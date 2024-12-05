from huggingface_hub import upload_folder

dataset_dir = "/app/output"
repo_id = "ej2/Holmes_data"
path_in_repo = "1"
msg = "upload dataset"
token = ""

upload_folder(repo_id = repo_id,
              folder_path = dataset_dir,
              path_in_repo=path_in_repo,
              commit_message=msg,
              token=token)