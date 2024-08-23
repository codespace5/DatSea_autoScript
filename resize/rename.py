import os
import random
import string
from PIL import Image

def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def save_as_png(image_path, output_folder):
    image_name = random_string(10) + ".png"
    output_path = os.path.join(output_folder, image_name)
    img = Image.open(image_path)
    img.save(output_path, "PNG")

def main(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".jfif") or filename.endswith(".png"):
            image_path = os.path.join(input_folder, filename)
            save_as_png(image_path, output_folder)

if __name__ == "__main__":
    input_folder = "./final"  # Change this to your input folder containing images
    output_folder = "6-5"   # Change this to the folder where you want to save the PNG files
    main(input_folder, output_folder)