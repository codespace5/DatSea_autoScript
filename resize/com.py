#    python com.py --background_folder background --object_folder object --result_folder rm


import os
import random
import argparse
from PIL import Image

# Define folders
background_folder = './background'
object_folder = './rm_object'
result_folder = 'result_folder'

# Ensure result folder exists
os.makedirs(result_folder, exist_ok=True)

# Function to overlay object image onto background image at random position
def overlay_images(background_path, object_path, result_path):
    # Open images
    background = Image.open(background_path)
    obj = Image.open(object_path)

    # Get dimensions
    bg_width, bg_height = background.size
    obj_width, obj_height = obj.size

    # Generate random position
    max_x = bg_width - obj_width
    max_y = bg_height - obj_height
    random_x = random.randint(0, max_x)
    random_y = random.randint(int(max_y/2), max_y)

    # Paste object onto background
    background.paste(obj, (random_x, random_y), obj if obj.mode == 'RGBA' else None)

    # Save result
    background.save(result_path)

if __name__ == "__main__":
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Overlay object images onto background images.")
    parser.add_argument("--background_folder", type=str, default="./background", help="Path to the folder containing background images.")
    parser.add_argument("--object_folder", type=str, default="./rm_object", help="Path to the folder containing object images.")
    parser.add_argument("--result_folder", type=str, default="result_folder", help="Path to the folder where result images will be saved.")
    args = parser.parse_args()

    # Set folder paths
    background_folder = args.background_folder
    object_folder = args.object_folder
    result_folder = args.result_folder

    # Ensure result folder exists
    os.makedirs(result_folder, exist_ok=True)

    # Get list of images in folders
    background_images = [f for f in os.listdir(background_folder) if os.path.isfile(os.path.join(background_folder, f))]
    object_images = [f for f in os.listdir(object_folder) if os.path.isfile(os.path.join(object_folder, f))]

    # Process each object image
    for obj_image in object_images:
        # Define path for object image
        object_path = os.path.join(object_folder, obj_image)

        # Process each background image with the current object image
        for bg_image in background_images:
            # Define paths
            background_path = os.path.join(background_folder, bg_image)
            result_path = os.path.join(result_folder, f'result_{obj_image.split(".")[0]}_{bg_image}')

            # Overlay images
            overlay_images(background_path, object_path, result_path)






# import os
# import random
# from PIL import Image

# # Define folders
# background_folder = './background'
# object_folder = './rm_object'
# result_folder = 'result_folder'

# # Ensure result folder exists
# os.makedirs(result_folder, exist_ok=True)

# # Function to overlay object image onto background image at random position
# def overlay_images(background_path, object_path, result_path):
#     # Open images
#     background = Image.open(background_path)
#     obj = Image.open(object_path)

#     # Get dimensions
#     bg_width, bg_height = background.size
#     obj_width, obj_height = obj.size

#     # Generate random position
#     max_x = bg_width - obj_width
#     max_y = bg_height - obj_height
#     random_x = random.randint(0, max_x)
#     random_y = random.randint(0, max_y)

#     # Paste object onto background
#     background.paste(obj, (random_x, random_y), obj if obj.mode == 'RGBA' else None)

#     # Save result
#     background.save(result_path)

# # Get list of images in folders
# background_images = [f for f in os.listdir(background_folder) if os.path.isfile(os.path.join(background_folder, f))]
# object_images = [f for f in os.listdir(object_folder) if os.path.isfile(os.path.join(object_folder, f))]

# # Process each object image
# for obj_image in object_images:
#     # Define path for object image
#     object_path = os.path.join(object_folder, obj_image)

#     # Process each background image with the current object image
#     for bg_image in background_images:
#         # Define paths
#         background_path = os.path.join(background_folder, bg_image)
#         result_path = os.path.join(result_folder, f'result_{obj_image.split(".")[0]}_{bg_image}')

#         # Overlay images
#         overlay_images(background_path, object_path, result_path)
