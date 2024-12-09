import os
import random
import string

def rename_files(folder_path):
    files = os.listdir(folder_path)
    for file_name in files:
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=15))
        file_extension = os.path.splitext(file_name)[1]
        new_file_name = random_name + file_extension
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
folder_path = './8.final_result'
rename_files(folder_path)