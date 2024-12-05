import os

from transformers import LlamaTokenizer
from datasets import Dataset, concatenate_datasets

dataset_dir = "/app/data"
output_dir = "/app/output"
num_workers = 6
from SkyDataProcess import SkyDataProcess
processor = SkyDataProcess

# 加载预训练模型的tokenizer
tokenizer = LlamaTokenizer.from_pretrained("model/", use_fast=True)
# 创建数据处理对象
data_process = processor(tokenizer)
# # 获取所有数据文件
data_process.get_all_data_files(dataset_dir)
# # 处理所有数据文件
data_process.process_all_files(num_workers)
# # conbine datasets
dataset_dirs = [os.path.join(dataset_dir, dataset) for dataset in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, dataset))]
concatenate_datasets([Dataset.load_from_disk(dataset) for dataset in dataset_dirs]).save_to_disk(output_dir)
                