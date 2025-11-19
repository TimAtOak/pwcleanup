import os

from get_folder_size import get_folder_size


def log_folders(path):
    # List all files and folders in the directory
    entries = os.listdir(path)
    size_list = []

    for entry in entries:
        full_path = os.path.join(path, entry)
        try:
            if os.path.isfile(full_path):
                size = os.path.getsize(full_path)
            elif os.path.isdir(full_path):
                size = get_folder_size(full_path)
            else:
                continue
            size_list.append((entry, size))
        except (FileNotFoundError, PermissionError):
            continue

    min_size = 5 * 1024 * 1024  # 5 MB

    # Sort and filter
    sorted_list = sorted(
        (item for item in size_list if item[1] >= min_size),
        key=lambda x: x[1],
        reverse=True
    )

    if not sorted_list:
        print("No big files or folders found!")
        return

    # Print nicely
    for name, size in sorted_list:
        if os.path.isdir(os.path.join(path, name)):
            type_str = "Folder"
        else:
            type_str = "File"
        print(f"{type_str}: {name} - {size / (1024*1024):.2f} MB")

