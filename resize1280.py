import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def resize_images(input_folder, output_folder, width, height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', 'jfif')):  # Check for image files
            file_path = os.path.join(input_folder, filename)
            
            with Image.open(file_path) as img:
                img_resized = img.resize((width, height))
                img_resized.save(os.path.join(output_folder, filename))

    messagebox.showinfo("Success", "Images have been resized and saved in the result folder.")

def select_input_folder():
    folder = filedialog.askdirectory()
    if folder:
        input_folder_var.set(folder)

def select_output_folder():
    folder = filedialog.askdirectory()
    if folder:
        output_folder_var.set(folder)

def start_resizing():
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()
    width = width_var.get()
    height = height_var.get()

    if not input_folder or not output_folder:
        messagebox.showerror("Error", "Both input and output folders must be selected.")
        return
    
    if not width.isdigit() or not height.isdigit():
        messagebox.showerror("Error", "Width and height must be positive integers.")
        return
    
    resize_images(input_folder, output_folder, int(width), int(height))

# Create the main window
root = tk.Tk()
root.title("Image Resizer")

# Create StringVar variables to hold the folder paths and dimensions
input_folder_var = tk.StringVar()
output_folder_var = tk.StringVar()
width_var = tk.StringVar(value="1280")
height_var = tk.StringVar(value="960")

# Create and place the input folder widgets
input_label = tk.Label(root, text="Input Folder:")
input_label.grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(root, textvariable=input_folder_var, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=10)
input_button = tk.Button(root, text="Browse...", command=select_input_folder)
input_button.grid(row=0, column=2, padx=10, pady=10)

# Create and place the output folder widgets
output_label = tk.Label(root, text="Output Folder:")
output_label.grid(row=1, column=0, padx=10, pady=10)
output_entry = tk.Entry(root, textvariable=output_folder_var, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=10)
output_button = tk.Button(root, text="Browse...", command=select_output_folder)
output_button.grid(row=1, column=2, padx=10, pady=10)

# Create and place the width and height widgets
width_label = tk.Label(root, text="Width:")
width_label.grid(row=2, column=0, padx=10, pady=10)
width_entry = tk.Entry(root, textvariable=width_var, width=10)
width_entry.grid(row=2, column=1, padx=10, pady=10, sticky='w')

height_label = tk.Label(root, text="Height:")
height_label.grid(row=2, column=1, padx=10, pady=10, sticky='e')
height_entry = tk.Entry(root, textvariable=height_var, width=10)
height_entry.grid(row=2, column=2, padx=10, pady=10)

# Create and place the resize button
resize_button = tk.Button(root, text="Resize Images", command=start_resizing)
resize_button.grid(row=3, column=0, columnspan=3, pady=20)

# Run the application
root.mainloop()
