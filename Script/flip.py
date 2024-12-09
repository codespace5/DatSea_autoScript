import os
from PIL import Image

source_folder = './2.size_changed'
output_folder = './3.flipped'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(source_folder):
    try:
        if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp', '.jfif', '.avif')):
            image_path = os.path.join(source_folder, filename)
            image = Image.open(image_path).convert("RGB")
            flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
            flipped_image_path = os.path.join(output_folder, "." +  filename)
            flipped_image.save(flipped_image_path)
    except IOError:
        print(f"File not found or cannot process: {filename}. Skipping...")
        continue