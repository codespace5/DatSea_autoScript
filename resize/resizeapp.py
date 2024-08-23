import os
import argparse
from PIL import Image

# Define the argument parser
parser = argparse.ArgumentParser(description='Resize images in a directory.')
parser.add_argument('input_dir', type=str, help='Path to the input directory containing images.')
parser.add_argument('output_dir', type=str, help='Path to the output directory to save resized images.')
args = parser.parse_args()

# Ensure output directories exist
size_categories = ['30-60', '60-160', '160-200']
for category in size_categories:
    os.makedirs(os.path.join(args.output_dir, category), exist_ok=True)

# Function to resize image while maintaining aspect ratio
def resize_image(image, min_size, max_size):
    width, height = image.size
    aspect_ratio = width / height
    
    if width > height:
        new_width = min(max(min_size, width), max_size)
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = min(max(min_size, height), max_size)
        new_width = int(new_height * aspect_ratio)
    
    return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

# Process each image in the input directory
for filename in os.listdir(args.input_dir):
    if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'jfif')):
        image_path = os.path.join(args.input_dir, filename)
        image = Image.open(image_path)

        # Resize and save images in each category
        for category in size_categories:
            min_size, max_size = map(int, category.split('-'))
            resized_image = resize_image(image, min_size, max_size)
            resized_image.save(os.path.join(args.output_dir, category, filename))

print("Images have been resized and saved in the respective directories.")






# import os
# from PIL import Image

# # Define the input and output directories
# input_dir = './origin'
# output_dir = './result_resize'

# # Ensure output directories exist
# size_categories = ['30-60', '60-160', '160-200']
# for category in size_categories:
#     os.makedirs(os.path.join(output_dir, category), exist_ok=True)

# # Function to resize image while maintaining aspect ratio
# def resize_image(image, min_size, max_size):
#     width, height = image.size
#     aspect_ratio = width / height
    
#     if width > height:
#         new_width = min(max(min_size, width), max_size)
#         new_height = int(new_width / aspect_ratio)
#     else:
#         new_height = min(max(min_size, height), max_size)
#         new_width = int(new_height * aspect_ratio)
    
#     return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

# # Process each image in the input directory
# for filename in os.listdir(input_dir):
#     if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
#         image_path = os.path.join(input_dir, filename)
#         image = Image.open(image_path)

#         # Resize and save images in each category
#         for category in size_categories:
#             min_size, max_size = map(int, category.split('-'))
#             resized_image = resize_image(image, min_size, max_size)
#             resized_image.save(os.path.join(output_dir, category, filename))

# print("Images have been resized and saved in the respective directories.")
