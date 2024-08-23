import os
import argparse
from PIL import Image

def resize_images(input_folder, output_folder, width=1280, height=960):
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', 'PNG', 'JPG', 'jfif')):  # Check for image files
            # Construct full file path
            file_path = os.path.join(input_folder, filename)
            
            # Open an image file
            with Image.open(file_path) as img:
                # Resize image
                img_resized = img.resize((width, height))
                
                # Save the resized image to the output folder
                img_resized.save(os.path.join(output_folder, filename))

    print("Images have been resized and saved in the result folder.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize images to 1280x960 and save to the output folder.")
    parser.add_argument("input_folder", type=str, help="Path to the input folder containing images.")
    parser.add_argument("output_folder", type=str, help="Path to the output folder to save resized images.")

    args = parser.parse_args()
    
    resize_images(args.input_folder, args.output_folder)
