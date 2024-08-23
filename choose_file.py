import os
import shutil
import csv

# Specify the input CSV file
csv_file = 'pass.csv'

# Specify the source directory
source_dir = './KH179'

# Specify the destination directory
destination_dir = './Passed'

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Read the file paths from the CSV file
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        relative_path = row[0]
        source_file = relative_path
        if os.path.exists(source_file):
            # Construct the destination file path
            destination_file = os.path.join(destination_dir, relative_path)
            # Create the destination directory if it doesn't exist
            destination_dir_path = os.path.dirname(destination_file)
            if not os.path.exists(destination_dir_path):
                os.makedirs(destination_dir_path)
            # Copy the file
            shutil.move(source_file, destination_file)
            print(f"Copied: {source_file} to {destination_file}")
        else:
            print(f"File not found: {source_file}")