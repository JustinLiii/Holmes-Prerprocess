from fire import Fire
from huggingface_hub import upload_folder

def main(repo_id: str, path_in_repo: str, upload_folder: str = "/app/output", msg: str = "upload dataset", token: str = ""):
    upload_folder(repo_id = repo_id,
                folder_path = upload_folder,
                path_in_repo=path_in_repo,
                commit_message=msg,
                token=token)
    
if __name__ == "__main__":
    Fire(main)