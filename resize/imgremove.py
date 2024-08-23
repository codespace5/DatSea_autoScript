#  python imgremove.py --input_dir object --output_dir rmb

import os
import cv2
import argparse
from rembg import remove

def remove_background(input_dir, output_dir):
    # Make sure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Process each file in the input directory
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)

        # Check if the file is an image (you can add more extensions if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', 'jfif')):
            # Read the input image
            input_image = cv2.imread(input_path)

            # Remove the background
            output_image = remove(input_image)

            # Define the output path with .png extension
            output_filename = os.path.splitext(filename)[0] + '.png'
            output_path = os.path.join(output_dir, output_filename)

            # Save the output image as a PNG file
            cv2.imwrite(output_path, output_image)

    print("Background removal and saving as PNG completed for all images.")

if __name__ == "__main__":
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Remove background from images.")
    parser.add_argument("--input_dir", type=str, default="./object", help="Path to the directory containing input images.")
    parser.add_argument("--output_dir", type=str, default="./rm_object", help="Path to the directory where output images will be saved.")
    args = parser.parse_args()

    # Set input and output directories
    input_dir = args.input_dir
    output_dir = args.output_dir

    # Perform background removal
    remove_background(input_dir, output_dir)









# import os
# import cv2
# from rembg import remove

# # Define the input and output directories
# input_dir = './object'
# output_dir = './rm_object'

# # Make sure the output directory exists
# os.makedirs(output_dir, exist_ok=True)

# # Process each file in the input directory
# for filename in os.listdir(input_dir):
#     input_path = os.path.join(input_dir, filename)

#     # Check if the file is an image (you can add more extensions if needed)
#     if filename.lower().endswith(('.png', '.jpg', '.jpeg','JPG', 'PNG','jfif')):
#         # Read the input image
#         input_image = cv2.imread(input_path)

#         # Remove the background
#         output_image = remove(input_image)

#         # Define the output path with .png extension
#         output_filename = os.path.splitext(filename)[0] + '.png'
#         output_path = os.path.join(output_dir, output_filename)

#         # Save the output image as a PNG file
#         cv2.imwrite(output_path, output_image)

# print("Background removal and saving as PNG completed for all images.")





# import os
# import cv2
# from rembg import remove

# # Define the input and output directories
# input_dir = './object'
# output_dir = './res_object'

# # Make sure the output directory exists
# os.makedirs(output_dir, exist_ok=True)

# # Process each file in the input directory
# for filename in os.listdir(input_dir):
#     input_path = os.path.join(input_dir, filename)

#     # Check if the file is an image (you can add more extensions if needed)
#     if filename.lower().endswith(('.png', '.jpg', '.jpeg', 'JPG', 'PNG','jfif')):
#         # Read the input image
#         input_image = cv2.imread(input_path)

#         # Remove the background
#         output_image = remove(input_image)

#         # Define the output path
#         output_path = os.path.join(output_dir, filename)

#         # Save the output image
#         cv2.imwrite(output_path, output_image)

# print("Background removal completed for all images.")
