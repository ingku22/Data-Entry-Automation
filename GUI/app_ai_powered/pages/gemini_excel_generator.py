# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
# from tkinter import *
from tkinter import Canvas, Button, PhotoImage, Frame, BOTH, Text, Entry, Label, messagebox, END
from backend.excel_methods import ExcelHandler
from segmentation import format_to_excel
import webbrowser

excel_handler = ExcelHandler()

class gemini_excel_generator:
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def __init__(self, root):

        BASE_PATH = Path(__file__).resolve().parent.parent

        # Define the relative path to the assets directory
        ASSETS_REL_PATH = Path("assets/frame3")

        # Define the absolute path to the assets directory
        self.ASSETS_PATH = BASE_PATH / ASSETS_REL_PATH

        self.window = Frame(root)

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 550,
            width = 700,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            700.0,
            62.0,
            fill="#00116B",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            62.0,
            281.0,
            550.0,
            fill="#313131",
            outline="")

        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            491.0,
            306.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            490.0,
            221.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            490.0,
            458.0,
            image=self.image_image_3
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.window,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: excel_handler.changeSheet(-1, self.canvas, self.label, 300, 107.5, 380, 245),
            relief="flat"
        )
        self.button_1.place(
            x=407.0,
            y=83.0,
            width=20.0,
            height=20.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.window,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: excel_handler.changeSheet(1, self.canvas, self.label, 300, 107.5, 380, 245),
            relief="flat"
        )
        self.button_2.place(
            x=555.0,
            y=83.0,
            width=20.0,
            height=20.0
        )

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            491.0,
            93.0,
            image=self.image_image_4
        )

        self.label=self.canvas.create_text(
            428.0,
            84.0,
            anchor="nw",
            text="Sheet 1",
            fill="#FFFFFF",
            font=("Inter Bold", 14 * -1)
        )

        self.canvas.create_text(
            490.0,
            393.0,
            anchor="nw",
            text="Export Excel ",
            fill="#1E2BA3",
            font=("Inter Bold", 16 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            393.0,
            458.5,
            image=self.entry_image_1
        )
        self.excel_stat = Text(
            self.canvas,
            bd=0,
            bg="#8D8D8D",
            fg="#000716",
            highlightthickness=0,
            pady=5,
            font=('Arial', 9)
        )
        self.excel_stat.place(
            x=320.0,
            y=389.0,
            width=146.0,
            height=137.0
        )

        self.canvas.create_text(
            491.0,
            425.0,
            anchor="nw",
            text="File Name:",
            fill="#1E2BA3",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            579.0,
            457.5,
            image=self.entry_image_2
        )
        self.file_name_entry = Entry(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.file_name_entry.place(
            x=500.0,
            y=445.0,
            width=158.0,
            height=23.0
        )

        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.delete_excel_btn = Button(
            self.window,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.delete_excel_btn.place(
            x=490.0,
            y=479.0,
            width=60.0,
            height=45.0
        )

        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.download_btn = Button(
            self.window,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.download_btn.place(
            x=550.0,
            y=480.0,
            width=118.0,
            height=45.0
        )

        self.canvas.create_text(
            21.0,
            14.0,
            anchor="nw",
            text="Excel Generator",
            fill="#FFFFFF",
            font=("Inter Bold", 28 * -1)
        )

        self.button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(
            self.window,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.copy_to_clipboard,
            relief="flat"
        )
        self.button_5.place(
            x=174.0,
            y=86.0,
            width=87.0,
            height=21.0
        )   

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            142.0,
            278.5,
            image=self.entry_image_3
        )
        self.text_formatted_menu = Text(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            pady=10,
            font=('Arial', 10)
        )
        self.text_formatted_menu.place(
            x=37.0,
            y=117.0,
            width=210.0,
            height=321.0
        )

        self.button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        self.generate_btn = Button(
            self.window,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.generate_btn.place(
            x=21.0,
            y=485.0,
            width=242.0,
            height=49.0
        )

        self.image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            630.0,
            28.0,
            image=self.image_image_5
        )

        self.button_image_7 = PhotoImage(
            file=self.relative_to_assets("button_7.png"))
        self.button_7 = Button(
            self.window,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: webbrowser.open("https://gemini.google.com/app"),
            relief="flat"
        )
        self.button_7.place(
            x=20.0,
            y=76.0,
            width=140.0,
            height=31.0
        )

        self.button_image_8 = PhotoImage(
            file=self.relative_to_assets("button_8.png"))
        self.button_8 = Button(
            self.window,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=self.add_category,
            relief="flat"
        )
        self.button_8.place(
            x=22.0,
            y=447.0,
            width=105.0,
            height=31.0
        )

        self.button_image_9 = PhotoImage(
            file=self.relative_to_assets("button_9.png"))
        self.button_9 = Button(
            self.window,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=self.add_option_group,
            relief="flat"
        )
        self.button_9.place(
            x=132.0,
            y=447.0,
            width=130.0,
            height=31.0
        )

        self.init_button_commands()

    def copy_to_clipboard(self):
        text_to_copy = "Extract the Menu Items and Costs from the menu image. First Identify the Category as 'category'. Then format them in this particular way 'Menu item - costs' with no cost denotations or descriptions. If there are more than one cost for a menu item, put it in this order 'cost 1, cost 2, cost 3', else if there are choices, put them in a bracket as such '(choice 1: cost 1, choice 2: cost 2, choice 3: cost 3)'"
        self.window.clipboard_clear()
        self.window.clipboard_append(text_to_copy)
        self.window.update()

        # Hide button 5
        self.button_5.place_forget()

        # Label to notify that text has been copied
        self.copied_label = Label(
            self.window,
            text="Copied!",
            bg="#313131",
            fg="#FFFFFF"
        )
        self.copied_label.place(
            x=164.0,
            y=82.0,
            width=100.0,
            height=21.0
        )

        # Revert the button back to "Copy Prompt" after 1s
        self.window.after(1000, self.revert_button)

    def revert_button(self):
        self.copied_label.destroy()

        # Place back the button
        self.button_5.place(
            x=174.0,
            y=86.0,
            width=87.0,
            height=21.0
        )

    # ============================== DIRECT BACKEND ===============================
    # init functions
    def init_button_commands(self):
        self.generate_btn.config(command=self.generate_excel)
        self.delete_excel_btn.config(command=self.remove_excel)
        self.download_btn.config(command=self.download_excel)


    # Text format editor
    def add_category(self):
        print('Added Category')
        self.text_formatted_menu.insert(END, '\n!')

    def add_option_group(self):
        print('Added Option Group')
        self.text_formatted_menu.insert(END, '\n?')

    # Excel Function
    # Methodology (per image in images):
    # get image path -> ocr -> ocr sorting -> transfer into dataframe -> transfer into treeview -> display treeview
    def generate_excel(self):
        print('Generating Excel File')

        # If there is a current excel, try to remove it to prevent syntax errors
        try:
            self.remove_excel(show_error=False)
        except:
            pass

        ## Copy input when Generate Excel button is clicked and convert
        text_to_convert = self.text_formatted_menu.get("1.0", 'end-1c')
        data, columns, stats = format_to_excel(text_to_convert)
        
        excel_handler.dataframe_to_excel(data, columns)
        excel_handler.loadSheet(self.canvas, self.label, 300, 107.5, 380, 245)
        # transfer into treeview
        # self.excel_preview_table = get_ttk_table(root=self.window, width=380)
        # self.excel_preview_table.place(
        #     x=300.0,
        #     y=107.5,
        #     height=245
        # )

        # show statistics of the treeview
        DUMMY_STATS_DATA = f'''GENERATED REPORT
=================
Category: {stats['Category']}
Menu Items: {stats['Menu Items']}
Option grp: {stats['Option Groups']}
Options: {stats['Options']}
        
File Size: 4KB'''
        
        self.excel_stat.delete(1.0, END)
        self.excel_stat.insert(END, DUMMY_STATS_DATA)
        self.excel_stat.config(state='disabled')
        self.download_btn.config(state='normal')


    def remove_excel(self, show_error=True):
        print('Excel Removed.')
        try:
            excel_handler.deleteSheet()
            self.excel_stat.config(state='normal')
            self.excel_stat.delete(1.0, END)
            self.canvas.itemconfig(self.label, text="") 

            self.file_name_entry.delete(0, END)
            self.download_btn.config(state='disabled')
        except:
            if show_error:
                messagebox.showerror(title='AttributeError', message='application has no attribute "excel_preview_table".')


    def download_excel(self):
        set_file_name = self.file_name_entry.get().lstrip().rstrip()
        # Check for missing values
        if set_file_name not in ['', None]:
            # download the file
            self.excel_name = set_file_name
            print(f'File Name: {self.excel_name}')

            text_to_convert = self.text_formatted_menu.get("1.0", 'end-1c')
            data, columns, stats = format_to_excel(text_to_convert)

            excel_handler.download_named_excel(data, columns, self.excel_name)
            messagebox.showinfo(title='Success',
                                    message=f'{self.excel_name}.xlsx Downloaded Successfully')
        else:
            messagebox.showerror(title='DataFormatError',
                                    message='Please name your excel file.')


    # Page Functions
    def run(self):
        self.window.resizable(False, False)
        self.window.mainloop()

    def pack(self):
        self.window.pack(fill=BOTH, expand=True)

    def pack_forget(self):
        self.window.pack_forget()
