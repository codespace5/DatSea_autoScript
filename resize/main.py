import os
import cv2
from rembg import remove
from PIL import Image
import random
import argparse
from datetime import datetime

background_path = './background'
resized_backround_path = './resized_background'
object_path = './objects'
resize_object_path = './resize_object'
object_remove_background = './remove_object'
size_categories = ['30-60', '90-160', '180-200']
# size_categories = ['180-210']

result_path = './results'

def remove_background(input_dir, output_dir):
    # Make sure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Process each file in the input directory
    for filename in os.listdir(input_dir):
        print('background removing', filename)
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

def object_resize(background_path, resized_backround_path):

    for category in size_categories:
        os.makedirs(os.path.join(resized_backround_path, category), exist_ok=True)

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
    for filename in os.listdir(background_path):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'jfif')):
            image_path = os.path.join(background_path, filename)
            image = Image.open(image_path)

            # Resize and save images in each category
            for category in size_categories:
                min_size, max_size = map(int, category.split('-'))
                resized_image = resize_image(image, min_size, max_size)
                resized_image.save(os.path.join(resized_backround_path, category, filename))


    print('background resized')

def background_resize(input_folder, output_folder, width=1280, height=960):
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

def overlay_images(background_path, object_path, result_path, img_name):
    # Open images
    background = Image.open(background_path)
    obj = Image.open(object_path)

    # Get dimensions
    bg_width, bg_height = background.size
    obj_width, obj_height = obj.size

    current_time = datetime.now()
    seed = current_time.hour * 3600 + current_time.minute * 60 + current_time.second
    random.seed(seed*10)

    # Generate random position
    max_x = bg_width - obj_width
    max_y = bg_height - obj_height
    random_x = random.randint(0, max_x)
    # random_y = random.randint(int(max_y/4), int(max_y*3/4))
    random_y = random.randint(int(max_y*2/3), int(max_y*9/10))
    # Paste object onto background
    background.paste(obj, (random_x, random_y), obj if obj.mode == 'RGBA' else None)

    # Save result as PNG using img_name
    background.save(os.path.join(result_path, f'{img_name}.png'), 'PNG')

def combine_images(background_folder, object_folder, result_folder, img_name='img'):
    background_images = [f for f in os.listdir(background_folder) if os.path.isfile(os.path.join(background_folder, f))]
    object_images = [f for f in os.listdir(object_folder) if os.path.isfile(os.path.join(object_folder, f))]

    # Process each object image
    os.makedirs(result_folder, exist_ok=True)
    num = 0
    for obj_image in object_images:
        # Define path for object image
        print('processing image', obj_image)
        object_path = os.path.join(object_folder, obj_image)

        # Process each background image with the current object image
        for bg_image in background_images:
            # Define paths
            background_path = os.path.join(background_folder, bg_image)
            # img_name = f'result_{obj_image.split(".")[0]}_{bg_image.split(".")[0]}'

            # Overlay images

            overlay_images(background_path, object_path, result_folder, img_name + '_' + str(num))
            num += 1

    print("Images combined and saved as PNG files.")

def main(name):
    # remove_background(object_path, object_remove_background)

    print('\n\n ################################################# \n')
    is_continue = input('Please check removed object results. If you want to continue, please insert Y keyward.\n')
    if is_continue == 'y':
        background_resize(background_path, resized_backround_path, 1280, 960)
        # object_resize(object_remove_background, resize_object_path)
        # for object in os.listdir(resize_object_path):
        for object in os.listdir(object_path):
            save_path = os.path.join(result_path, object)
            os.makedirs(save_path, exist_ok=True)
            print('save path', save_path)
            path1 = resize_object_path + '/' + object + '/'
            combine_images(resized_backround_path, path1, save_path, name)
            print("test", object)

        print("complete")
    else:
        print('please try again')

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description="resize")
    parse.add_argument("name", type=str, help="image name")

    args = parse.parse_args()
    main(args.name)





# import os
# import cv2
# from rembg import remove
# from PIL import Image
# import random

# background_path = './background'
# resized_backround_path = './resized_background'
# object_path = './objects'
# resize_object_path = './resize_object'
# object_remove_background = './remove_object'
# size_categories = ['30-60', '60-160', '160-200']

# result_path = './results'

# def remove_background(input_dir, output_dir):
#     # Make sure the output directory exists
#     os.makedirs(output_dir, exist_ok=True)

#     # Process each file in the input directory
#     for filename in os.listdir(input_dir):
#         print('background removing', filename)
#         input_path = os.path.join(input_dir, filename)

#         # Check if the file is an image (you can add more extensions if needed)
#         if filename.lower().endswith(('.png', '.jpg', '.jpeg', 'jfif')):
#             # Read the input image
#             input_image = cv2.imread(input_path)

#             # Remove the background
#             output_image = remove(input_image)

#             # Define the output path with .png extension
#             output_filename = os.path.splitext(filename)[0] + '.png'
#             output_path = os.path.join(output_dir, output_filename)

#             # Save the output image as a PNG file
#             cv2.imwrite(output_path, output_image)

#     print("Background removal and saving as PNG completed for all images.")

# def object_resize(background_path, resized_backround_path):

#     for category in size_categories:
#         os.makedirs(os.path.join(resized_backround_path, category), exist_ok=True)

#     # Function to resize image while maintaining aspect ratio
#     def resize_image(image, min_size, max_size):
#         width, height = image.size
#         aspect_ratio = width / height
        
#         if width > height:
#             new_width = min(max(min_size, width), max_size)
#             new_height = int(new_width / aspect_ratio)
#         else:
#             new_height = min(max(min_size, height), max_size)
#             new_width = int(new_height * aspect_ratio)
        
#         return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

#     # Process each image in the input directory
#     for filename in os.listdir(background_path):
#         if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'jfif')):
#             image_path = os.path.join(background_path, filename)
#             image = Image.open(image_path)

#             # Resize and save images in each category
#             for category in size_categories:
#                 min_size, max_size = map(int, category.split('-'))
#                 resized_image = resize_image(image, min_size, max_size)
#                 resized_image.save(os.path.join(resized_backround_path, category, filename))


#     print('background resized')

# def background_resize(input_folder, output_folder, width=1280, height=960):
#     # Create the output folder if it does not exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Iterate over all files in the input folder
#     for filename in os.listdir(input_folder):
#         if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', 'PNG', 'JPG', 'jfif')):  # Check for image files
#             # Construct full file path
#             file_path = os.path.join(input_folder, filename)
            
#             # Open an image file
#             with Image.open(file_path) as img:
#                 # Resize image
#                 img_resized = img.resize((width, height))
                
#                 # Save the resized image to the output folder
#                 img_resized.save(os.path.join(output_folder, filename))

#     print("Images have been resized and saved in the result folder.")
   

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
#     random_y = random.randint(int(max_y/2), max_y)

#     # Paste object onto background
#     background.paste(obj, (random_x, random_y), obj if obj.mode == 'RGBA' else None)

#     # Save result as PNG
#     background.save(result_path, 'PNG')


# def combine_images(background_folder, object_folder, result_folder):
#     background_images = [f for f in os.listdir(background_folder) if os.path.isfile(os.path.join(background_folder, f))]
#     object_images = [f for f in os.listdir(object_folder) if os.path.isfile(os.path.join(object_folder, f))]

#     # Process each object image
#     os.makedirs(result_folder, exist_ok=True)
#     for obj_image in object_images:
#         # Define path for object image
#         print('processing image', obj_image)
#         object_path = os.path.join(object_folder, obj_image)

#         # Process each background image with the current object image
#         for bg_image in background_images:
#             # Define paths
#             background_path = os.path.join(background_folder, bg_image)
#             result_path = os.path.join(result_folder, f'result_{obj_image.split(".")[0]}_{bg_image.split(".")[0]}.png')

#             # Overlay images
#             overlay_images(background_path, object_path, result_path)

#     print("Images combined and saved as PNG files.")






# def main():
#     background_resize(background_path, resized_backround_path, 1280, 960)
#     remove_background(object_path, object_remove_background)
#     object_resize(object_remove_background, resize_object_path)
#     for object in os.listdir(resize_object_path):
#         save_path = os.path.join(result_path, object)
#         os.makedirs(save_path, exist_ok = True)
#         print('save path', save_path)
#         path1 = resize_object_path + '/' + object + '/'
#         combine_images(resized_backround_path,  path1, save_path)
#         print("test", object)

#     print("complete")


# if __name__ == '__main__':
#     main()


