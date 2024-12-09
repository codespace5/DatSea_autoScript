import os
from PIL import Image

min_size = 640
current_dir = os.getcwd()
image_dir = '0.origin_images'
resized_dir = '2.size_changed'
image_dir = os.path.join(current_dir, image_dir)
resized_dir = os.path.join(current_dir, resized_dir)

for filename in os.listdir(image_dir):
    try:
        img = Image.open(os.path.join(image_dir, filename))
        width, height = img.size
        if width < height:
            if width < min_size:
                new_width = min_size
                new_height = int((height / width) * new_width)
            else:
                new_width = width
                new_height = height
        else:
            if height < min_size:
                new_height = min_size
                new_width = int((width / height) * new_height)
            else:
                new_width = width
                new_height = height

        img = img.resize((new_width, new_height))
        img.save(os.path.join(resized_dir, filename))
        
    except IOError:
        print(f"File not found: {filename}. Skipping...")
        continue
