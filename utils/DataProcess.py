from concurrent.futures import ProcessPoolExecutor

import numpy as np

class DataProcess:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.max_length = 4096
        self.data_files = []
    
    def get_all_data_files(self, data_dir):
        raise NotImplementedError
    
    def process_one_file(self, data_path):
        raise NotImplementedError
    
    def process_all_files(self, max_workers=6):
        # self.precess_one_file(self.data_files[0])
        # 使用多进程处理文件
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            # 提交所有文件处理任务到进程池
            executor.map(self.process_one_file, self.data_files)
            # 等待所有任务完成
        print("All files processed.")
                    
    
    def tokenize_sentense(self, sentence):
        start_token = self.tokenizer.bos_token
        end_token = self.tokenizer.eos_token

        sentence_with_tokens = f"{start_token} {sentence} {end_token}"
            
        # 将句子转换为 token ids
        tokens = self.tokenizer.encode(sentence_with_tokens, add_special_tokens=False, 
                                truncation=True, max_length=self.max_length)
            
        return tokens

    def convert_list_to_numpy(self, input_list, dtype=np.uint16):
        # 所有数字均在 0-65535 之间
        return np.array(input_list, dtype=dtype)