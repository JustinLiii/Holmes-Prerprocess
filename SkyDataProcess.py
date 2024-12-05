import os
import json

from tqdm import tqdm
from datasets import Dataset

from utils.DataProcess import DataProcess

class SkyDataProcess(DataProcess):
    
    @staticmethod
    def _get_processed_files(data_dir: str) -> list:
        processed_files = set(file for file in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, file)))
        return list(processed_files)
    
    def get_all_data_files(self, data_dir):
        # 获取所有json文件
        processed_files = self._get_processed_files(data_dir)
        all_files = os.listdir(data_dir)
        self.data_files = [os.path.join(data_dir, file) for file in all_files if file.endswith(".jsonl") and file.strip(".jsonl") not in processed_files]
        print(f"{len(self.data_files)} files to process. Total {len(self.data_files) + len(processed_files)} files.")
    
    def process_one_file(self, data_path, context=200):
        # 每一行都是一个json对象，读取里面的text字段
        array = []
        with open(data_path, "r", encoding="utf-8") as f:
            current_tokens = []
            # for every sentence
            for line in tqdm(f):
                sentence = json.loads(line)["text"]
                tokens = self.tokenize_sentense(sentence)
                current_tokens += tokens
                if len(current_tokens) > self.max_length:
                    exceed_tokens = current_tokens[self.max_length:]  # 截取超出部分
                    not_exceed_tokens = current_tokens[:self.max_length]  # 截断到 max_length
                    npy = self.convert_list_to_numpy(not_exceed_tokens)
                    array.append({"input_ids": npy})
                    
                    # 判断损失的下文多少
                    if len(exceed_tokens) < context:
                        current_tokens = []
                    else:
                        current_tokens = exceed_tokens

        # 最后一行填充到 self.max_length 并加入结果列表
        if current_tokens:
            current_tokens += [self.tokenizer.pad_token_id] * (self.max_length - len(current_tokens))
            npy = self.convert_list_to_numpy(current_tokens)
            array.append({"input_ids": npy})
            
        path = data_path.split(".")[0]
        dataset = Dataset.from_list(array)
        dataset.save_to_disk(path)