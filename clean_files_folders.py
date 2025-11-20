import os
import shutil


def clean_files_folders(path):
    """Delete all files and subfolders inside a folder, but keep the folder."""
    if not os.path.isdir(path):
        return False, f"Not a folder: {path}"

    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)

            if os.path.isdir(item_path):
                shutil.rmtree(item_path)  # delete subfolder
            else:
                os.remove(item_path)  # delete file

        return True, f"Emptied folder: {path}"

    except Exception as e:
        return False, f"Error: {e}"