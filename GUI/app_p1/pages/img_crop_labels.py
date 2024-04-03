# This file was built of the Generation from Tkinter Designer by Parth Jadhav

# ---------------------------
# Imports
# ---------------------------
from pathlib import Path
import ast
from PIL import Image, ImageTk

from tkinter import Tk, ttk, messagebox, Canvas, Entry, Text, Button, PhotoImage, Frame, Radiobutton
from tkinter import BOTH, END, LEFT, StringVar
from idlelib.tooltip import Hovertip
from backend.table_methods import get_ttk_table, tree_add_data, tree_remove_all_data
# from backend.data_methods import
from backend.file_methods import display_select_file, resize, zip_n_download

class img_crop_label:
    def relative_to_assets(self, path: str) -> Path:
        # Return the full path by joining ASSETS_PATH with the provided relative path
        return self.ASSETS_PATH / Path(path)
    
    def __init__(self, root):

        BASE_PATH = Path(__file__).resolve().parent.parent

        # Define the relative path to the assets directory
        ASSETS_REL_PATH = Path("assets/frame1")
        STAGING_REL_PATH = Path("assets/staging")

        # Define the absolute path to the assets directory
        self.ASSETS_PATH = BASE_PATH / ASSETS_REL_PATH
        self.STAGING_PATH = BASE_PATH / STAGING_REL_PATH

        self.window = Frame(root)
        self.crop_mode = False
        self.crop_type = StringVar(value="Items")

        self.current_image = None # PhotoImage Tk
        self.current_image_ref = None # PIL Image (Cropping Reference)
        self.current_image_path = None

        self.current_crop = None
        self.ratio_coordinates = None # (x1 %pos, y1 %pos, %width, %height) for resized image + cropping
        self.coordinates = None # (x1, y1, x2, y2) based on cropped image pixels
        self.crops_info = {}

        self.canvas = Canvas(
            self.window,
            bg = "#D2D2D2",
            height = 550,
            width = 700,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            211.0,
            306.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            700.0,
            62.0,
            fill="#00116B",
            outline="")

        self.canvas.create_text(
            13.0,
            14.0,
            anchor="nw",
            text="Manual Menu Labeller",
            fill="#FFFFFF",
            font=("Inter Bold", 28 * -1)
        )

        # Insert Image Panel
        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            210.0,
            245.0,
            image=self.image_image_3
        )


        # Label and Export Frame
        # ========================================================

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            210.0,
            485.0,
            image=self.image_image_2
        )

        self.crop_type_text = self.canvas.create_text(
            25.0,
            467.0,
            anchor="nw",
            text="Category Name",
            fill="#1E2BA3",
            font=("Arial", 11)
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            271.5,
            476.5,
            image=self.entry_image_1
        )
        self.category_name_entry = Entry(
            self.window,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.category_name_entry.place(
            x=156.0,
            y=464.0,
            width=231.0,
            height=23.0
        )

        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.add_cropped_label_btn = Button(
            self.window,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.add_cropped_label_btn.place(
            x=259.0,
            y=496.0,
            width=137.0,
            height=32.0
        )

        self.add_cropped_tip = Hovertip(self.add_cropped_label_btn,
                                        'Add Cropped Label and Category Name\nCrop Data will appear in the data table on your right', hover_delay=10)
        # ===========================================

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.browse_files_btn = Button(
            self.window,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.browse_files_btn.place(
            x=146.0,
            y=306.0,
            width=128.0,
            height=32.0
        )

        self.browse_files_tip = Hovertip(self.browse_files_btn,
                                         'Button to import images.\nImages uploaded will not dissapear unless replaced with another image.', hover_delay=10)

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        self.image_placeholder = self.canvas.create_image(
            210.0,
            232.0,
            image=self.image_image_4
        )

        self.image_visual = Canvas(
            self.window,
            bg = "#D2D2D2",
            height = 300,
            width = 350,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        # self.image_visual.place(x=(210.0 - 350/2), y= (247.0 - 300/2))


        self.canvas.create_text(
            25.0,
            436.0,
            anchor="nw",
            text="Confirm Cropped Label",
            fill="#1E2BA3",
            font=("Arial", 14)
        )

        self.canvas.create_rectangle(
            422.0,
            62.0,
            700.0,
            550.0,
            fill="#292929",
            outline="")

        self.canvas.create_rectangle(
            435.0,
            68.0,
            687.0,
            160.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            435.0,
            168.0,
            687.0,
            306.0,
            fill="#373737",
            outline="")

        self.canvas.create_rectangle(
            435.0,
            321.0,
            687.0,
            482.0,
            fill="#363636",
            outline="")

        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.download_folder_btn = Button(
            self.window,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.download_folder_btn.place(
            x=540.0,
            y=493.0,
            width=147.0,
            height=46.0
        )

        # self.download_folder_btn.config(state='disable')
        self.download_folder_tip = Hovertip(self.download_folder_btn,
                                            'Press here to download the zip file of all your cropped menu categories.\nAll the image data in the table will be included in your downloaded zip file', hover_delay=10)

        self.button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        self.clear_all_btn = Button(
            self.window,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.clear_all_btn.place(
            x=435.0,
            y=494.0,
            width=97.0,
            height=46.0
        )

        self.clear_all_tip = Hovertip(self.clear_all_btn,
                                     'Deletes all table data of cropped images.\nCrops on the Image and in the data table will be deleted', hover_delay=10)

        self.button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        self.zoom_in_btn = Button(
            self.window,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.zoom_in_btn.place(
            x=445.0,
            y=127.0,
            width=25.0,
            height=25.0
        )

        self.button_image_7 = PhotoImage(
            file=self.relative_to_assets("button_7.png"))
        self.zoom_out_btn = Button(
            self.window,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self.zoom_out_btn.place(
            x=475.0,
            y=127.0,
            width=25.0,
            height=25.0
        )

        self.button_image_8 = PhotoImage(
            file=self.relative_to_assets("button_8.png"))
        self.add_crop_btn = Button(
            self.window,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command= self.init_cropping,
            relief="flat"
        )
        self.add_crop_btn.place(
            x=443.0,
            y=98.0,
            width=96.33131408691406,
            height=26.304079055786133
        )

        self.add_crop_tip = Hovertip(self.add_crop_btn,
                                     'Activates CROP MODE\nAllows you to crop images. Only active when no current crop is made.\nTo enable the Add Crop Button, ensure that all previous crops have been labelled and added to the table.\n Yellow - Unlabelled\nGreen - Labelled', hover_delay=10)

        self.button_image_9 = PhotoImage(
            file=self.relative_to_assets("button_9.png"))
        self.delete_crop_btn = Button(
            self.window,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=self.delete_cropping,
            relief="flat"
        )
        self.delete_crop_btn.place(
            x=543.0,
            y=98.0,
            width=111.0,
            height=25.0
        )

        self.delete_crop_tip = Hovertip(self.delete_crop_btn,
                                     'Deletes Selected Crop\nOnly active if a crop data is selecte.\nTo enable the Delete Crop Button, ensure that you have selected a crop to delete in the data table below.', hover_delay=10)

        self.canvas.create_text(
            444.0,
            75.0,
            anchor="nw",
            text="Label/Image Editor",
            fill="#8F8F8F",
            font=("MS Sans Serif", 12)
        )

        # Menu Category Data Init
        LABEL_COLUMNS = ['Category', 'Cropped Dimensions']
        LABEL_DATA = [['--', '(-, -, -, -)']]
        # LABEL_DATA = [
        #     ['Appetizers', '[35,35,35,35]'],
        #     ['Drinks', '[35,35,35,35]'],
        #     ['Soups', '[35,35,35,35]'],
        #     ['Main Dish', '[35,35,35,35]'],
        #     ['Pizza Toppings', '[35,35,35,35]'],
        #     ['Specials', '[35,35,35,35]'],
        #     ['Desserts', '[35,35,35,35]'],
        #     ['Retail', '[35,35,35,35]']
        # ]

        # Menu Category Data Table
        self.canvas.create_text(
            444.0,
            322.0,
            anchor="nw",
            text="Menu Categories",
            fill="#8F8F8F",
            font=("MS Sans Serif", 12)
        )

        self.cropped_label_table = get_ttk_table(root=self.window , width=230, 
                                            column=LABEL_COLUMNS,
                                            data=LABEL_DATA)
        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview', background='#808080', fieldbackground='#000000', 
                        foreground='#FFFFFF', bordercolor='#A7A7A7')

        style.configure('Treeview.Heading', background='#000000', foreground='#FFFFFF',
                        bordercolor='#A7A7A7')


        self.cropped_label_table.place(
            x=444.0,
            y=346.0,
            height=130
        )

        self.button_image_10 = PhotoImage(
            file=self.relative_to_assets("button_10.png"))
        self.button_10 = Button(
            self.window,
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_10.place(
            x=535.0,
            y=127.0,
            width=106.0,
            height=25.0
        )

        self.button_10_tip = Hovertip(self.button_10,
                                     'Button to import images.\nImages uploaded will not dissapear unless replaced with another image.', hover_delay=10)

        self.image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        self.crop_not_found = self.canvas.create_image(
            559.0,
            226.0,
            image=self.image_image_5,
            tag=('crop_not_found')
        )

        self.cropped_image_visual = Canvas(
            self.window,
            bg = "#D2D2D2",
            height = 130,
            width = 244,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        # self.cropped_image_visual.place(x=560-(244/2), y=236-(130/2))


        self.button_image_11 = PhotoImage(
            file=self.relative_to_assets("button_11.png"))
        self.refresh_btn = Button(
            self.window,
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_11 clicked"),
            relief="flat"
        )
        self.refresh_btn.place(
            x=505.0,
            y=127.0,
            width=25.0,
            height=25.0
        )

        self.refresh_tip = Hovertip(self.refresh_btn,
                                     'Refreshes the Image to its original fullsize.\nAll Cropped Plots are also displayed on the Image.', hover_delay=10)

        self.button_image_12 = PhotoImage(
            file=self.relative_to_assets("button_12.png"))
        self.remove_img_btn = Button(
            self.window,
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.remove_img_btn.place(
            x=646.0,
            y=127.0,
            width=25.0,
            height=25.0
        )

        self.remove_img_tip = Hovertip(self.remove_img_btn,
                                     'Button to remove images.\nImage will be removed along with the table data.', hover_delay=10)
        

        # Create a frame to hold the radio buttons
        self.crop_type_frame = Frame(self.window, bg='blue')  # Set the width of the frame

        # Create and pack the radio buttons with padding
        option1_button = Radiobutton(self.crop_type_frame, text="Menu Item", variable=self.crop_type, value="Items", padx=5, 
                                        font=('Arial', 11), bg='#D9D9D9',
                                        command=self.change_crop_type)  # Add padding to the left and right
        option1_button.pack(side=LEFT)

        option2_button = Radiobutton(self.crop_type_frame, text="Option Group", variable=self.crop_type, value="Options", padx=5, 
                                        font=('Arial', 11), bg='#D9D9D9',
                                        command=self.change_crop_type)  # Add padding to the left and right
        option2_button.pack(side=LEFT)

        self.crop_type_frame.place(
            x=25.0,
            y=500.0
        )

        self.button_image_13 = PhotoImage(
            file=self.relative_to_assets("button_13.png"))
        self.stage_crops_btn = Button(
            self.window,
            image=self.button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_13 clicked"),
            relief="flat"
        )
        self.stage_crops_btn.place(
            x=578.0,
            y=323.0,
            width=107.0,
            height=18.0
        )

        self.init_button_commands()

    # ======================= BACKEND ======================

    # Display/Remove Image
    def display_original_img(self):
        img_w = 350
        img_l = 300
        tk_image, size, image_ref, filepath = display_select_file(target_width=img_w, target_height=img_l)
        
        
        if f'{tk_image}'[:-2] == 'pyimage':
            width, height = size

            self.image_visual.config(width=width, height=height)
            self.current_image = self.image_visual.create_image(width/2, height/2, image=tk_image)
            self.current_image_ref = image_ref
            self.current_image_path = filepath

            self.image_visual.place(x=(210.0 - width/2), y= (247.0 - height/2))
            self.browse_files_btn.place_forget()

            # Keep a reference to tk_image to prevent garbage collection
            self.canvas.tk_image = tk_image

    def remove_original_img(self):
        self.image_visual.place_forget()
        self.browse_files_btn.place(
                x=146.0,
                y=306.0,
                width=128.0,
                height=32.0
            )

    def init_button_commands(self):
        self.browse_files_btn.config(command=self.display_original_img)
        self.button_10.config(command=self.display_original_img)
        self.remove_img_btn.config(command=self.remove_original_img)
        self.add_cropped_label_btn.config(command=self.verify_cropped_label_data)

        self.download_folder_btn.config(command=lambda dwnld=True: self.saved_cropped_img(download=dwnld))
        self.stage_crops_btn.config(command=self.saved_cropped_img)
        
        self.clear_all_btn.config(command=self.clear_all_label_data)
        self.cropped_label_table.bind("<ButtonRelease-1>", self.select_crop)
        # self.cropped_label_table.bind("<<TreeviewSelect>>", self.on_treeview_select)

        # self.add_cropped_label_btn.bind('<Return>', lambda event: self.verify_cropped_label_data())
        # self.window.focus_set()

    def change_crop_type(self):
        if self.crop_type.get() == 'Items':
            print('Cropping for Menu Items.')
            self.canvas.itemconfig(self.crop_type_text, text='Category Name')

        elif self.crop_type.get() == 'Options':
            print('Cropping for Option Groups.')
            self.canvas.itemconfig(self.crop_type_text, text='Option Group')


    # Save Cropped Images
    def saved_cropped_img(self, download=False):
        string_info = 'Items saved into staging folder:\n'

        for category, crop_stats in self.crops_info.items():
            _, coords = crop_stats
            cropped_img, _ = self.get_cropped_image(coords)
            cropped_img.save(self.STAGING_PATH / f'{category}.jpg')

            string_info += f'\n{category}.jpg'

        messagebox.showinfo(
            title='SaveInfo',
            message=string_info
        )

        if download:
            zip_n_download(self.STAGING_PATH)
            messagebox.showinfo(
                title='SaveInfo',
                message='Staging Folder has been downloaded!'
            )

    # obtaining/verifying cropped label row data

    def verify_cropped_label_data(self):
        cropped_label = [self.category_name_entry.get(), str(self.ratio_coordinates)]

        if (type(cropped_label[0]) == str) and (type(cropped_label[1]) == str) and type(ast.literal_eval(cropped_label[1])) in [list, tuple]:

            if len(ast.literal_eval(cropped_label[1])) == 4:
                # send it to add_data to the update table
                print('Data Updated')
                print(cropped_label)
                
                self.crops_info[cropped_label[0]] = [self.current_crop, self.ratio_coordinates]
                print(self.crops_info)
                tree_add_data(data=cropped_label, table=self.cropped_label_table)

                self.category_name_entry.delete(0, END)
                self.coordinates = None
                self.ratio_coordinates = None

                # Enable Crop Mode again
                self.crop_mode = True
                print('Crop Mode is On')

                self.image_visual.bind("<ButtonPress-1>", self.start_cropping)
                self.image_visual.bind("<B1-Motion>", self.draw_rectangle)
                self.image_visual.bind("<ButtonRelease-1>", self.end_cropping)

            else:
                messagebox.showerror(title='DataFormatError',
                                    message='A dimension coordinate seems to be missing.')

        else:
            print('Data failed to update')
            messagebox.showerror(title='PostError',
                                    message='The form you have tried to submit is not compatible with the system.')
            

    def clear_all_label_data(self):
        tree_remove_all_data(table=self.cropped_label_table)
        for rect in self.crops_info.values():
            self.image_visual.delete(rect[0])

        self.crop_not_found = self.canvas.create_image(
            559.0,
            226.0,
            image=self.image_image_5,
            tag=('crop_not_found')
        )

        self.cropped_image_visual.place_forget()

        self.crops_info.clear()

    def on_treeview_select(self, event):
        selected_item = self.cropped_label_table.focus()
        if selected_item:
            category = self.cropped_label_table.item(selected_item, option="values")[0]

        print(category)


    def select_crop(self, event):
        # Highlight Crop on Image
        # item = int(self.cropped_label_table.selection()[0][1:])
        selected_item = self.cropped_label_table.focus()
        if selected_item:
            category = self.cropped_label_table.item(selected_item, option="values")[0]

        if category == '--':
            for r in self.crops_info.values():
                self.image_visual.itemconfig(r[0], outline="lime")  # Reset all outlines
                self.crop_not_found = self.canvas.create_image(
                    559.0,
                    226.0,
                    image=self.image_image_5,
                    tag=('crop_not_found')
                )
                self.cropped_image_visual.place_forget()

        elif category in list(self.crops_info.keys()):
            rect, coords = self.crops_info[category]
            for r in self.crops_info.values():
                self.image_visual.itemconfig(r[0], outline="lime")  # Reset all outlines
            self.image_visual.itemconfig(rect, outline="blue")   # Set selected outline to blue

            # Display Cropped Image on Preview
            self.canvas.delete("crop_not_found")
            cropped_img, size = self.get_cropped_image(coords)
            resized_cropped_img, size = resize(cropped_img, target_width=244, target_height=130)
            tk_cropped_image = ImageTk.PhotoImage(resized_cropped_img)

            if f'{tk_cropped_image}'[:-2] == 'pyimage':
                width, height = size

                self.cropped_image_visual.delete('all')
                self.cropped_image_visual.config(width=width, height=height)
                self.cropped_image_visual.create_image(width/2, height/2, image=tk_cropped_image)
                

                self.cropped_image_visual.place(x=(560 - width/2), y= (236 - height/2))
                print('placed cropped_image_visual')

                # Keep a reference to tk_image to prevent garbage collection
                self.canvas.tk_cropped_image = tk_cropped_image
            

        else:
            print("Error: Selected item not found in crop dictionary")

    # --------------------------------     
    # CROPPING FUNCTIONS
    # --------------------------------
    
    def get_cropped_image(self, coords):
        if coords:
            with Image.open(self.current_image_path) as img:
                image_width, image_height = img.size

                # Calculate pixel coordinates
                x1 = int(coords[0] * image_width)
                y1 = int(coords[1] * image_height)
                x2 = int(x1 + coords[2] * image_width)
                y2 = int(y1 + coords[3] * image_height)

                # Crop image
                cropped_img = img.crop((x1, y1, x2, y2))

        return cropped_img, (x2-x1, y2-y1)

    # Methodology
    # crop mode -> crop -> rename the category, add the category, shows up as image + add table

    def init_cropping(self):
        print('Initializing Cropping...')

        if self.crop_mode == False:
            self.crop_mode = True
            print('Crop Mode is On')

            self.image_visual.bind("<ButtonPress-1>", self.start_cropping)
            self.image_visual.bind("<B1-Motion>", self.draw_rectangle)
            self.image_visual.bind("<ButtonRelease-1>", self.end_cropping)

        elif self.crop_mode == True:
            self.crop_mode = False
            print('Crop Mode is Off')

            self.image_visual.unbind("<ButtonPress-1>")
            self.image_visual.unbind("<B1-Motion>")
            self.image_visual.unbind("<ButtonRelease-1>")

    def start_cropping(self, event):
        self.start_x = self.image_visual.canvasx(event.x)
        self.start_y = self.image_visual.canvasy(event.y)
        self.current_crop = self.image_visual.create_rectangle(self.start_x, self.start_y, self.start_x, 
                                                      self.start_y, outline="yellow", width=4)

    def draw_rectangle(self, event):
        cur_x = self.image_visual.canvasx(event.x)
        cur_y = self.image_visual.canvasy(event.y)
        self.image_visual.coords(self.current_crop, self.start_x, self.start_y, cur_x, cur_y)

    def end_cropping(self, event):

        # Disable crop mode
        self.crop_mode = False
        self.image_visual.unbind("<ButtonPress-1>")
        self.image_visual.unbind("<B1-Motion>")
        self.image_visual.unbind("<ButtonRelease-1>")

        image_width = self.image_visual.winfo_width()
        image_height = self.image_visual.winfo_height()

        end_x = min(max(event.x, 0), image_width)
        end_y = min(max(event.y, 0), image_height)
        self.image_visual.itemconfig(self.current_crop, outline="lime")
        x1 = min(self.start_x, end_x)
        y1 = min(self.start_y, end_y)
        x2 = max(self.start_x, end_x)
        y2 = max(self.start_y, end_y)

        crop_width = x2 - x1
        crop_height = y2 - y1

        self.coordinates = (x1, y1, x2, y2)
        self.ratio_coordinates = (round(x1/image_width, 5), 
                                  round(y1/image_height, 5),
                                  round(crop_width/image_width, 5),
                                  round(crop_height/image_height, 5))

        # Calculate the width and height of the cropped area
        

        print(f'Cropped: {self.ratio_coordinates}')
        self.adjust_cropping()

    def adjust_cropping(self):
        x1, y1, x2, y2 = self.coordinates
        self.image_visual.coords(self.current_crop, x1, y1, x2, y2)

    def delete_cropping(self):
        selected_item = self.cropped_label_table.focus()
        if selected_item:
            category = self.cropped_label_table.item(selected_item, option="values")[0]

            if category != '--' and category in self.crops_info:
                selected_crop = self.crops_info[category][0]
                self.image_visual.delete(selected_crop)
                self.cropped_label_table.delete(selected_item)  # Delete the selected row
                self.cropped_image_visual.delete('all')
                self.crop_not_found = self.canvas.create_image(
                    559.0,
                    226.0,
                    image=self.image_image_5,
                    tag=('crop_not_found')
                )
                self.cropped_image_visual.place_forget()
                
                del self.crops_info[category]



    # ------------------------
    # PAGINATION FUNCTIONS
    # ------------------------
    def run(self):
        self.window.resizable(False, False)
        self.window.mainloop()

    def pack(self):
        self.window.pack(fill=BOTH, expand=True)

    def pack_forget(self):
        self.window.pack_forget()



# Page = img_crop_label()
# Page.run()