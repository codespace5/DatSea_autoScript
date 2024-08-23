import pandas as pd
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def process_images(file_path, output_folder, start_row, end_row, log_file):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    df = pd.read_csv(file_path)

    selected_rows = df.iloc[start_row - 2 : end_row-1]

    with open(log_file, 'a') as log:
        for index, row in selected_rows.iterrows():
            image_path = row[2]  # Assuming the third column is at index 2
            try:
                img = Image.open(image_path)
                print(image_path)
                img_name = os.path.basename(image_path)
                output_path = os.path.join(output_folder, img_name)
                img.save(output_path)
                print(f"Saved image {img_name} to {output_path}")
            except FileNotFoundError:
                print(f"Image not found: {image_path}")
                log.write(f"{image_path}\n")
            except Exception as e:
                print(f"Error processing image {image_path}: {e}")

def select_csv_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        entry_csv_path.delete(0, tk.END)
        entry_csv_path.insert(0, file_path)

def select_output_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_output_folder.delete(0, tk.END)
        entry_output_folder.insert(0, folder_path)

def start_processing():
    file_path = entry_csv_path.get()
    output_folder = entry_output_folder.get()
    log_file = entry_log_file.get()
    start_row = int(entry_start_row.get())
    end_row = int(entry_end_row.get())

    if not file_path or not output_folder or not log_file:
        messagebox.showerror("Error", "Please fill all the fields.")
        return

    process_images(file_path, output_folder, start_row, end_row, log_file)
    messagebox.showinfo("Success", "Image processing completed.")

root = tk.Tk()
root.title("Image Processor")

tk.Label(root, text="CSV File Path:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_csv_path = tk.Entry(root, width=50)
entry_csv_path.grid(row=0, column=1, padx=10, pady=5)
btn_browse_csv = tk.Button(root, text="Browse", command=select_csv_file)
btn_browse_csv.grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Output Folder:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_output_folder = tk.Entry(root, width=50)
entry_output_folder.grid(row=1, column=1, padx=10, pady=5)
btn_browse_output = tk.Button(root, text="Browse", command=select_output_folder)
btn_browse_output.grid(row=1, column=2, padx=10, pady=5)

tk.Label(root, text="Log File Path:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_log_file = tk.Entry(root, width=50)
entry_log_file.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Start Row:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
entry_start_row = tk.Entry(root, width=10)
entry_start_row.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
entry_start_row.insert(0, "10")

tk.Label(root, text="End Row:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
entry_end_row = tk.Entry(root, width=10)
entry_end_row.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)
entry_end_row.insert(0, "50")

btn_start = tk.Button(root, text="Start Processing", command=start_processing)
btn_start.grid(row=5, column=0, columnspan=3, pady=20)

root.mainloop()
