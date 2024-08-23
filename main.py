import os
import shutil
import random
import string
import tkinter as tk
from tkinter import filedialog, messagebox, Checkbutton, IntVar
from PIL import Image

def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def resize_and_rename_images(input_folder, output_folder, width, height, rename):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', 'jfif')):
            file_path = os.path.join(input_folder, filename)
            with Image.open(file_path) as img:
                img_resized = img.resize((width, height))
                if rename:
                    new_filename = generate_random_string() + os.path.splitext(filename)[1]
                else:
                    new_filename = filename
                img_resized.save(os.path.join(output_folder, new_filename))

    messagebox.showinfo("Success", "Images have been processed and saved in the output folder.")

def select_folder(entry):
    folder = filedialog.askdirectory()
    if folder:
        entry.delete(0, 'end')
        entry.insert(0, folder)

def start_processing():
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()
    width = width_var.get()
    height = height_var.get()
    rename = rename_var.get()

    if not input_folder or not output_folder:
        messagebox.showerror("Error", "Both input and output folders must be selected.")
        return

    if not width.isdigit() or not height.isdigit():
        messagebox.showerror("Error", "Width and height must be positive integers.")
        return
    
    resize_and_rename_images(input_folder, output_folder, int(width), int(height), rename)

# Create the main window
root = tk.Tk()
root.title("Image Resizer and Renamer")

# Create StringVar variables to hold the folder paths and dimensions
input_folder_var = tk.StringVar()
output_folder_var = tk.StringVar()
width_var = tk.StringVar(value="1280")
height_var = tk.StringVar(value="960")
rename_var = IntVar()

# Create and place the input and output folder widgets
labels = ["Input Folder:", "Output Folder:"]
entries = [input_folder_var, output_folder_var]
for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=10)
    entry = tk.Entry(root, textvariable=entries[i], width=50)
    entry.grid(row=i, column=1, padx=10, pady=10)
    button = tk.Button(root, text="Browse...", command=lambda e=entry: select_folder(e))
    button.grid(row=i, column=2, padx=10, pady=10)

# Width and height
tk.Label(root, text="Width:").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=width_var, width=10).grid(row=2, column=1, padx=10, pady=10, sticky='w')
tk.Label(root, text="Height:").grid(row=2, column=1, padx=10, pady=10, sticky='e')
tk.Entry(root, textvariable=height_var, width=10).grid(row=2, column=2, padx=10, pady=10)

# Rename checkbox
rename_check = Checkbutton(root, text="Rename Images", variable=rename_var)
rename_check.grid(row=3, column=0, columnspan=3)

# Resize and rename button
process_button = tk.Button(root, text="Process Images", command=start_processing)
process_button.grid(row=4, column=0, columnspan=3, pady=20)

# Run the application
root.mainloop()
