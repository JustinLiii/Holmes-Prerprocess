import os
from concurrent.futures import ThreadPoolExecutor

import wget

FILE_DIR = "/app/data"

def get_file(url):  
    file_name = url.strip().split("/")[-1]
    file_name = os.path.join(FILE_DIR, file_name)
    wget.download(url, file_name)

if __name__ == "__main__":
    
    with open("urls.txt", "r", encoding="utf-8") as f:
        urls = f.readlines()

    urls = [url.strip() for url in urls if url.strip().split("/")[-1] not in os.listdir(FILE_DIR)]
    total = len(urls)
    with ThreadPoolExecutor() as executor:
        for i, _ in enumerate(executor.map(get_file, urls)):
            print(f"\n{i+1}/{total}")