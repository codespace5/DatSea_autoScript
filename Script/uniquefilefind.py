import os
from collections import defaultdict

def find_unique_files(folder_path):

    file_dict = defaultdict(list)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            base_name, _ = os.path.splitext(file)
            file_path = os.path.join(root, file)
            file_dict[base_name].append(file_path)

    for base_name, file_paths in file_dict.items():
        if len(file_paths) == 1:
            print(f"Unique file: {file_paths[0]}")

root_folder = './test'
find_unique_files(root_folder)