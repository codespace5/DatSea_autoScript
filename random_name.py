import os
import random
import string
import shutil  # Import shutil for copying files
from tkinter import filedialog, messagebox, Tk, Label, Button, Entry, Frame

def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def rename_images(source_folder, save_folder):
    """Rename images in the source folder and save them in the specified save folder."""
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for filename in os.listdir(source_folder):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            image_path = os.path.join(source_folder, filename)
            file_extension = os.path.splitext(image_path)[1]
            random_string = generate_random_string()
            new_filename = random_string + file_extension
            new_path = os.path.join(save_folder, new_filename)
            shutil.copy2(image_path, new_path)  # Copy the image instead of moving it
    
    messagebox.showinfo("Success", "All images have been successfully copied and renamed.")

def select_folder(entry):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry.delete(0, 'end')
        entry.insert(0, folder_selected)

# Setting up the GUI
root = Tk()
root.title("Image Renamer Tool")

frame_source = Frame(root)
frame_source.pack(pady=10)

label_source = Label(frame_source, text="Source Folder:")
label_source.pack(side='left', padx=5)

entry_source = Entry(frame_source, width=50)
entry_source.pack(side='left', padx=5)

Button(frame_source, text="Select", command=lambda: select_folder(entry_source)).pack(side='left', padx=5)

frame_save = Frame(root)
frame_save.pack(pady=10)

label_save = Label(frame_save, text="Save Folder:")
label_save.pack(side='left', padx=5)

entry_save = Entry(frame_save, width=50)
entry_save.pack(side='left', padx=5)

Button(frame_save, text="Select", command=lambda: select_folder(entry_save)).pack(side='left', padx=5)

Button(root, text="Start Renaming", command=lambda: rename_images(entry_source.get(), entry_save.get())).pack(pady=20)

root.mainloop()
