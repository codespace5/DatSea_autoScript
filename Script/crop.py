import os
from PIL import Image

source_folder = './4.rotated'
output_folder = './5.cropped'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(source_folder):
    try:
        if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp', '.jfif', '.avif')):            
            image_path = os.path.join(source_folder, filename)
            image = Image.open(image_path)
            width, height = image.size
            width_1 = int(width * 0.88) 
            height_1 = int(height * 0.76)
            left = int(width * 0.06)
            top = int(height * 0.12)
            right = left + width_1
            bottom = top + height_1
            cropped_image = image.crop((left, top, right, bottom))
            output_path = os.path.join(output_folder, filename)
            cropped_image.save(output_path)
    except IOError:
        print(f"File not found: {filename}. Skipping...")
        continue