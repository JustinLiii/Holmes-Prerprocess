import huggingface_hub
from fire import Fire

def main(repo_id: str, allow_patterns: str, repo_type: str = "dataset", local_dir: str ="/app/data"):
    huggingface_hub.snapshot_download(
        repo_id=repo_id,
        repo_type=repo_type,
        allow_patterns=allow_patterns,
        local_dir=local_dir
    )
    
if __name__ == "__main__":
    Fire(main)