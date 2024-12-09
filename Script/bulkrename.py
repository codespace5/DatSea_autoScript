import os

folder_path = './3.flipped'
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp', '.jfif', '.avif')):        
        new_filename = "!" + filename
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))