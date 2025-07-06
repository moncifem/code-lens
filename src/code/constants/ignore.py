# Directories to ignore when walking through file system
IGNORED_DIRECTORIES = [
    '.venv',
    '__pycache__',
    '.git',
    'node_modules',
    '.idea',
    '.vscode',
    'dist',
    'build',
    '.pytest_cache',
    '.mypy_cache',
    '.tox',
    'coverage',
    'htmlcov',
    '.eggs',
    '*.egg-info',
    '.DS_Store',
    'Thumbs.db'
]

def should_ignore_directory(directory_name: str) -> bool:
    """Check if a directory should be ignored"""
    return directory_name in IGNORED_DIRECTORIES

def filter_directories(directories: list) -> list:
    """Filter out ignored directories from a list"""
    return [d for d in directories if not should_ignore_directory(d)]

def contains_ignored_path(path: str) -> bool:
    """Check if a path contains any ignored directory"""
    return any(ignore_dir in path for ignore_dir in IGNORED_DIRECTORIES) 