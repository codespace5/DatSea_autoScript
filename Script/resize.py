import os
from PIL import Image

source_folder = './5.cropped'
output_folder = './6.resized'

target_size = (1280,960)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(source_folder):
    try:
        if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp', '.jfif', '.avif')):  
            image_path = os.path.join(source_folder, filename)
            image = Image.open(image_path)
            width, height = image.size
            width_1 = int(width /0.88) 
            height_1 = int(height/ 0.76) 
            zoomed_image = image.resize((width_1, height_1), resample=Image.BICUBIC)
            resized_image = zoomed_image.resize(target_size, resample=Image.BICUBIC)
            output_path = os.path.join(output_folder, filename)
            resized_image.save(output_path)
    except IOError:
        print(f"File not found: {filename}. Skipping...")
        continue