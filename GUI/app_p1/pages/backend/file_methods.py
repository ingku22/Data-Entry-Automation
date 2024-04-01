from tkinter import filedialog, messagebox
import tkinter as tk
from PIL import Image, ImageTk

import os
import shutil
import zipfile
from pathlib import Path


SUPPORTED_FILE_TYPES = ['png', 'jpg', 'jpeg']

# --------------------------------     
# File to path FUNCTIONS
# --------------------------------



# --------------------------------     
# ZIP FILE FUNCTIONS
# --------------------------------
def zip_n_download(staging_path):
    # Create a zip file
    zip_filename = "staging.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        # Add all files and directories in the staging folder to the zip file
        for root, dirs, files in os.walk(staging_path):
            for file in files:
                file_path = Path(root) / file
                zipf.write(file_path, file_path.relative_to(staging_path))

    # Move the zip file to the user's Downloads directory
    downloads_path = Path.home() / "Downloads"
    shutil.move(zip_filename, downloads_path / zip_filename)
    print(f"Zip file saved to: {downloads_path / zip_filename}")

# --------------------------------     
# IMAGE FILE FUNCTIONS
# --------------------------------
def select_file():

    file_path = filedialog.askopenfilename()

    if file_path and file_path.split('.')[-1] in SUPPORTED_FILE_TYPES:
        print("Selected file:", file_path)

        # # Insert it into text area and another memory storage
            
            # Textbox.insert(tk.END, f'{file_path.split("/")[-1]}')
            # if len(num_images) - 2 < 3:
            #     Textbox.insert(tk.END, '\n')

        return file_path

    elif file_path:
        messagebox.showerror(title='TypeError',
                            message='File is not an image or is currently not supported by this application.')

    else:
        pass

def resize(img, target_width=None, target_height=None):
        original_width, original_height = img.size
        # Select how small to resize
        img_ratio = original_width / original_height # r > 1, img is landscape, r < 1, img is portriat

        if img_ratio > 1:
            target_width = target_width
            target_height = None
        elif img_ratio <= 1:
            target_width = None
            target_height = target_height

        # Resizing logic
        if target_width and not target_height:
            target_height = int((target_width / original_width) * original_height)
        elif target_height and not target_width:
            target_width = int((target_height / original_height) * original_width)
        resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
        
        width, height = resized_img.size
        print(f'size:{width}x{height}')

        return resized_img, (width, height)

def display_select_file(target_width=None, target_height=None, Container=None, archive_function=None):

    # Get the file path
    file_path = select_file()

    if archive_function:
        archive_function(Container, file_path)

    if file_path:
        # Resized Image for fitting with the visual display in the application
        with Image.open(file_path) as img:
            resized_img, size = resize(img, target_width=target_width, target_height=target_height)
        tk_image = ImageTk.PhotoImage(resized_img)

        return tk_image, size, resized_img, file_path

    else:
        print('filepath has not been defined')
        return None


def archive_to_textbox(Textbox, file_path):
    content = Textbox.get(1.0, tk.END)

    # Check if there is 3 images
    num_images = content.split('\n')
    if len(num_images) - 2 >= 3:
        print(num_images)
        messagebox.showerror(title='OverloadError',
                             message='This application currently only supports 3 images per run due to the processing time.')

    # Insert it into text area and another memory storage  
    Textbox.insert(tk.END, f'{file_path.split("/")[-1]}')
    if len(num_images) - 2 < 3:
        Textbox.insert(tk.END, '\n')