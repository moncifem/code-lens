# Downloader of git projects

from git import Repo
import os
try:
    from .logger import setup_logger
except ImportError:
    from logger import setup_logger

logger = setup_logger(name="git-downloader")

def download_repo(repo_url:str, path:str):
    if os.path.exists(path):
        logger.error(f"Folder {path} already exists")
        raise Exception(f"Folder {path} already exists")
    Repo.clone_from(repo_url, path)
    logger.info(f"Downloaded {repo_url} to {path}")

if __name__ == "__main__":
    repo_url = 'https://github.com/moncifem/code-lens.git'
    target_folder = './CodeLens'
    download_repo(repo_url, target_folder)