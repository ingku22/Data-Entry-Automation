
# This file was built of the Generation from Tkinter Designer by Parth Jadhav

# ---------------------------
# Imports
# ---------------------------
from pathlib import Path

import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, BOTH

# Backend imports
from backend.file_methods import select_file, display_select_file, archive_to_textbox


class image2excel:
    def relative_to_assets(self, path: str) -> Path:
        # Return the full path by joining ASSETS_PATH with the provided relative path
        return self.ASSETS_PATH / Path(path)

    def __init__(self, root):

        BASE_PATH = Path(__file__).resolve().parent.parent

        # Define the relative path to the assets directory
        ASSETS_REL_PATH = Path("assets/frame0")

        # Define the absolute path to the assets directory
        self.ASSETS_PATH = BASE_PATH / ASSETS_REL_PATH

        self.window = Frame(root)

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

        # ============================== FRONTEND ===============================

        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            350.0,
            306.0,
            image=self.image_image_1
        )

        # Generate Excel
        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.generate_btn = Button(
            self.window,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.process_tagging(),
            relief="flat"
        )


        self.generate_btn.place(
            x=30.0,
            y=477.0,
            width=168.0,
            height=49.0
        )

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            484.0,
            310.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            155.0,
            310.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            437.0,
            514.0,
            image=self.image_image_5
        )

        self.canvas.create_text(
            467.0,
            356.0,
            anchor="nw",
            text="File Name",
            fill="#1E2BA3",
            font=("Arial", 10)
        )
        self.canvas.create_text(
            467.0,
            334.0,
            anchor="nw",
            text="Export Excel ",
            fill="#1E2BA3",
            font=("Arial", 12)
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
            text="Menu to Excel Converter",
            fill="#FFFFFF",
            font=("Inter Bold", 28 * -1)
        )

        self.image_image_6 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            350.0,
            97.0,
            image=self.image_image_6
        )

        self.canvas.create_text(
            30.0,
            138.0,
            anchor="nw",
            text="File Upload",
            fill="#FFFFFF",
            font=("Arial", 14)
        )

        self.canvas.create_text(
            587.0,
            138.0,
            anchor="nw",
            text="Excel file",
            fill="#FFFFFF",
            font=("Arial", 14)
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            155.0,
            424.5,
            image=self.entry_image_1
        )
        self.entry_1 = Text(
            self.window,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Helvetica", 10)
        )
        self.entry_1.place(
            x=44.0,
            y=400.0,
            width=222.0,
            height=47.0
        )

        # Browse files
        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.window,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda Textbox=self.entry_1: self.display_preview(Textbox),
            relief="flat"
        )
        self.button_2.place(
            x=90.0,
            y=334.0,
            width=131.0,
            height=32.0
        )

        self.canvas.create_text(
            35.0,
            373.0,
            anchor="nw",
            text="Uploaded Files (Limit: 3)",
            fill="#1E2BA3",
            font=("Arial", 10)
        )

        self.image_image_7 = PhotoImage(
            file=self.relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            155.0,
            424.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=self.relative_to_assets("image_8.png")) # image_8 is default image for when not selected image
        self.image_visual = self.canvas.create_image(
            154.0,
            247.0,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file=self.relative_to_assets("image_9.png"))
        self.image_9 = self.canvas.create_image(
            384.0,
            393.0,
            image=self.image_image_9
        )

        self.image_image_10 = PhotoImage(
            file=self.relative_to_assets("image_10.png"))
        self.image_10 = self.canvas.create_image(
            384.0,
            393.0,
            image=self.image_image_10
        )

        # Delete Excel Output
        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.delete_btn = Button(
            self.window,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print('button_3 pressed'),
            relief="flat"
        )

        self.delete_btn.place(
            x=467.0,
            y=406.0,
            width=52.0,
            height=45.0
        )

        entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            384.5,
            394.0,
            image=entry_image_2
        )

        self.entry_2 = Text(
            self.window,
            bd=0,
            bg="#8D8D8D",
            fg="#000716",
            highlightthickness=0,
            font=("Helvetica", 10)
        )

        numm = '?'
        filler_data = ''
        menu_attr = ['category', 'menu items', 'opt groups', 'avg price']

        for attr in menu_attr:
            filler_data += f'{attr.upper():<11}{numm:>9}\n'
        filler_data += '\nFILE SIZE: 4KB'

        self.entry_2.delete(1.0, tk.END)
        self.entry_2.insert(tk.END, filler_data)
        self.entry_2.config(state='disabled')

        self.entry_2.place(
            x=314.0,
            y=340.0,
            width=141.0,
            height=106.0
        )

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            556.0,
            389.5,
            image=self.entry_image_3
        )
        self.file_name_entry = Entry(
            self.window,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.file_name_entry.place(
            x=477.0,
            y=377.0,
            width=158.0,
            height=23.0
        )

        # Return to left sheet
        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.previous_sheet_btn = Button(
            self.window,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.previous_sheet_btn.place(
            x=409.0,
            y=168.0,
            width=20.0,
            height=20.0
        )

        # Return to right excel sheet
        self.button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        self.next_excel_sheet = Button(
            self.window,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.next_excel_sheet.place(
            x=539.0,
            y=168.0,
            width=20.0,
            height=20.0
        )

        self.image_image_11 = PhotoImage(
            file=self.relative_to_assets("image_11.png"))
        self.image_11 = self.canvas.create_image(
            484.0,
            178.0,
            image=self.image_image_11
        )

        self.canvas.create_text(
            429.0,
            169.0,
            anchor="nw",
            text="Sheet 1",
            fill="#000000",
            font=("Arial", 10)
        )


        # Download Excel File
        self.button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        self.download_btn = Button(
            self.window,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.download_btn.place(
            x=527.0,
            y=407.0,
            width=118.0,
            height=45.0
        )

        self.download_btn.config(state='disabled')

        self.gen_status_label = self.canvas.create_text(
            208.0,
            491.0,
            anchor="nw",
            text="Generating...",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.loading_bar = self.canvas.create_text(
            208.0,
            508.0,
            anchor="nw",
            text="",
            fill="#C11B1B",
            font=("Inter Bold", 12 * -1)
        )

        # ============================== DIRECT BACKEND ===============================
    def display_preview(self, Textbox):
        tk_image, size, ref, filepath = display_select_file(Container=Textbox, target_width=200, target_height=130, archive_function=archive_to_textbox)
        self.canvas.itemconfig(self.image_visual, image=tk_image)

        # Keep a reference to tk_image to prevent garbage collection
        self.canvas.tk_image = tk_image

    # Set ERROR/INTERRUPTION status (testing)
    def set_status_error(self):
        current_gen_status = self.canvas.itemcget(self.gen_status_label, 'text')

        if current_gen_status[:6] == 'ERROR:':
            pass
        else:
            self.canvas.itemconfigure(self.gen_status_label, text='ERROR: KeyboardInterruption ')
        

    # Visual Loading function

    def process_tagging(self):
        init_loading_bar = self.canvas.itemcget(self.loading_bar, 'text')

        if len(init_loading_bar) != 0:
            self.canvas.itemconfigure(self.loading_bar, text='')

        self.canvas.itemconfigure(self.gen_status_label, text='Generating...')
        self.update_label()


    def update_label(self):
        process_dummy = ['Obtaining Menu Item', 'Locating Category', 'Extracting Costs', 
                    'Reading additional text elements', 'Locating Options', 'Finalizing Data Packet',
                    'Entering into Excel', 'Verifying Format']

        current_text = self.canvas.itemcget(self.loading_bar, 'text')
        current_gen_status = self.canvas.itemcget(self.gen_status_label, 'text')

        if current_gen_status[:6] == 'ERROR:':
            updated_text = current_text + '|'
            self.canvas.itemconfigure(self.loading_bar, text=updated_text)
            pass

        elif len(current_text) < 76:
            self.generate_btn.config(state='disabled')
            updated_text = current_text + "##"
            self.canvas.itemconfigure(self.gen_status_label, text=process_dummy[len(current_text)%len(process_dummy)]+'...')
            self.canvas.itemconfigure(self.loading_bar, text=updated_text)
            self.window.after(50, self.update_label)

        else:
            self.canvas.itemconfigure(self.gen_status_label, text='Completed!')
            self.generate_btn.config(state='active')

    def run(self):
        self.window.resizable(False, False)
        self.window.mainloop()

    def pack(self):
        self.window.pack(fill=BOTH, expand=True)

    def pack_forget(self):
        self.window.pack_forget()


# Page = image2excel()
# Page.run()