import os
import shutil
import argparse


###    python app.py --src dron --dest dron_output --name potter --start 55
def rename_images(src_folder, dest_folder, prefix, start):
    # Create destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    # Get a list of files in the source folder
    files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f))]
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.jfif', '.webp'))]

    # Sort the image files for consistent naming
    image_files.sort()

    for i, filename in enumerate(image_files, start=start):
        # Construct the new file name
        new_name = f"{prefix}_{i}{os.path.splitext(filename)[1]}"
        
        # Full path for source and destination files
        src_file = os.path.join(src_folder, filename)
        dest_file = os.path.join(dest_folder, new_name)
        
        # Copy and rename the file to the new destination
        shutil.copy2(src_file, dest_file)
        print(f"Renamed '{filename}' to '{new_name}' and saved to '{dest_folder}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Rename images with a specified prefix and starting number.')
    parser.add_argument('--src', type=str, required=True, help='Source folder containing images')
    parser.add_argument('--dest', type=str, required=True, help='Destination folder to save renamed images')
    parser.add_argument('--name', type=str, default='img', help='Prefix for renamed images')
    parser.add_argument('--start', type=int, default=1, help='Starting number for renamed images')

    args = parser.parse_args()

    rename_images(args.src, args.dest, args.name, args.start)
