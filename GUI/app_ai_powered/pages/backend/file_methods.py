from tkinter import filedialog, messagebox
import tkinter as tk
from PIL import Image, ImageTk

import os
import shutil
import zipfile
import json
from pathlib import Path


SUPPORTED_FILE_TYPES = ['png', 'jpg', 'jpeg']

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
    # os.mkdir(staging_path / 'staging')
    print(f"Zip file saved to: {downloads_path / zip_filename}")

def stage_json_setup(staging_path, dictionary):
    if os.path.exists(staging_path):
        with open(f'{staging_path}/label.json', 'w') as label_json:
            json.dump(dictionary, label_json)

        print('JSON file setup successfully!')

    else:
        print(f"The staging folder '{staging_path}' does not exist.")


def stage_destroy(staging_path):
    if os.path.exists(staging_path):
        # Remove all files in the staging folder
        for filename in os.listdir(staging_path):
            file_path = os.path.join(staging_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        print(f"The staging folder '{staging_path}' does not exist.")
# --------------------------------     
# IMAGE FILE FUNCTIONS
# --------------------------------
IMAGE_FILE_TYPES = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg']
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


# --------------------------------     
# FOLDER FUNCTIONS
# --------------------------------
DIR_SPECIAL_FILES = ['txt', 'json']

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        print("Selected folder:", folder_path)

    return folder_path

    
def obtain_folder_items(folder_path=None):

    if not folder_path: # Select folder mode
        folder_path = select_folder()

    if folder_path:
        directory_items = os.listdir(folder_path)
        special_files = []
        
        # Check for any special files
        for items in directory_items:
            if items.split('.')[-1] in DIR_SPECIAL_FILES:
                directory_items.remove(items)
                special_files.append(items)

        return directory_items, special_files
    
    else:
        print('No folder selected.')

    