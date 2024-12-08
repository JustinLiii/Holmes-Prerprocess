import os

from transformers import LlamaTokenizer
from datasets import Dataset, concatenate_datasets
from app.custom_files.MyDataProcess import MyDataProcess

def main(input_dir: str = "/app/data", output_dir: str = "/app/output", num_workers: int = 6):
    # 加载预训练模型的tokenizer
    tokenizer = LlamaTokenizer.from_pretrained("model/", use_fast=True)
    # 创建数据处理对象
    data_process = MyDataProcess(tokenizer)
    # # 获取所有数据文件
    data_process.get_all_data_files(input_dir)
    # # 处理所有数据文件
    data_process.process_all_files(num_workers)
    # # conbine datasets
    dataset_dirs = [os.path.join(input_dir, dataset) for dataset in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, dataset))]
    concatenate_datasets([Dataset.load_from_disk(dataset) for dataset in dataset_dirs]).save_to_disk(output_dir)
