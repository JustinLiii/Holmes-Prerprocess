import huggingface_hub

huggingface_hub.snapshot_download(
    repo_id="Skywork/SkyPile-150B",
    repo_type="dataset",
    allow_patterns="data/*",
    local_dir="/app/data"
)