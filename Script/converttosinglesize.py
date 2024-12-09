import os
from PIL import Image

source_folder = './1.converted_to_jpg'
output_folder = './2.size_changed'
target_size = (1280, 960)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(source_folder):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp', '.jfif', '.avif')):
        file_path = os.path.join(source_folder, filename)
        image = Image.open(file_path)
        resized_image = image.resize(target_size, resample=Image.BICUBIC)
        output_file_path = os.path.join(output_folder, filename)
        resized_image.save(output_file_path)