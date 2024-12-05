import os
from concurrent.futures import ThreadPoolExecutor

import wget
from fire import Fire

def get_file(url, file_dir):  
    file_name = url.strip().split("/")[-1]
    file_name = os.path.join(file_dir, file_name)
    wget.download(url, file_name)

def main(file_dir: str = "/app/data"):
    with open("urls.txt", "r", encoding="utf-8") as f:
        urls = f.readlines()
        
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    urls = [url.strip() for url in urls if url.strip().split("/")[-1] not in os.listdir(file_dir)]
    total = len(urls)
    with ThreadPoolExecutor() as executor:
        for i, _ in enumerate(executor.map(lambda x: get_file(x, file_dir), urls)):
            print(f"\n{i+1}/{total}")
            
if __name__ == "__main__":
    Fire(main)