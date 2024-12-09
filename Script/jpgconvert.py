import os
from PIL import Image

src_folder = './0.origin_images'
flip_folder = './3.flipped'
output_folder = './1.converted_to_jpg'

if not os.path.exists(flip_folder):
    os.makedirs(flip_folder)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def process_images_in_directory(src_folder, flip_folder, output_folder):
    for root, dirs, files in os.walk(src_folder):
        # Calculate relative path and create corresponding directory in flip_folder and output_folder
        relative_path = os.path.relpath(root, src_folder)
        current_flip_folder = os.path.join(flip_folder, relative_path)
        current_output_folder = os.path.join(output_folder, relative_path)
        
        if not os.path.exists(current_flip_folder):
            os.makedirs(current_flip_folder)
        if not os.path.exists(current_output_folder):
            os.makedirs(current_output_folder)

        for filename in files:
            try:
                if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp', '.jfif', '.avif')):
                    src_path = os.path.join(root, filename)
                    image = Image.open(src_path).convert("RGB")
                    flip_path = os.path.join(current_flip_folder, filename)            
                    temp_image = image.transpose(Image.FLIP_LEFT_RIGHT)
                    rotated_image = temp_image.transpose(Image.FLIP_LEFT_RIGHT)
                    rotated_image.save(flip_path)

                    dst_path = os.path.join(current_output_folder, os.path.splitext(filename)[0] + '.jpg')
                    rotated_image.save(dst_path, 'JPEG', quality=90)
                    os.remove(flip_path)
                else:
                    print(f"Skipping {filename} as it is not a supported image format.")
            except (IOError):
                print(f"Error processing {filename}. Skipping...")
                continue

# Start processing the images
process_images_in_directory(src_folder, flip_folder, output_folder)
