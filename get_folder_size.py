import os

def get_folder_size(path):
    """Recursively get total size of a folder in bytes"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                total_size += os.path.getsize(fp)
            except (FileNotFoundError, PermissionError):
                pass  # skip files we can't access
    return total_size