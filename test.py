
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
import pandas as pd
from tkinter import ttk, Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, filedialog

def uploadExcel():
    file_path = filedialog.askopenfilename(title="Select Excel file",
                                            filetypes=(("Excel files", "*.xlsx;*.xlsm;*.xml"), ("All files", "*.*")))

    if file_path:
        excel_file = pd.ExcelFile(file_path)
    print(excel_file.sheet_names)

uploadExcel()