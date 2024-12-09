import os
from PIL import Image

source_folder = './3.flipped'
output_folder = './4.rotated'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(source_folder):
    try:
        if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp', '.jfif', '.avif')):
            image_path = os.path.join(source_folder, filename)
            image = Image.open(image_path)
            rotated_image = image.rotate(-10)
            rotated_image_path = os.path.join(output_folder, "_" + filename)
            rotated_image.save(rotated_image_path)
    except IOError:
        print(f"File not found: {filename}. Skipping...")
        continue