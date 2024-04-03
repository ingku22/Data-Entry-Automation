from pathlib import Path
import pandas as pd
from tkinter import ttk, Frame, filedialog, PhotoImage
from backend.display_methods import hideElement, showElement

class ExcelHandler: 
            
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def __init__(self):
    
        BASE_PATH = Path(__file__).resolve().parent.parent

        # Define the relative path to the assets directory
        ASSETS_REL_PATH = Path("assets/frame2")

        self.ASSETS_PATH = BASE_PATH / ASSETS_REL_PATH
    
        self.excel_file = None
        self.sheetNo = 0
        self.file_path = ""
        self.frame = None
    

    def changeSheet(self, adj, canvas, label):
        num_of_sheets = len(self.excel_file.sheet_names)
        if self.sheetNo + adj >= 0 and self.sheetNo + adj < num_of_sheets:
            self.sheetNo += adj
            self.loadSheet(canvas, label)

    def uploadExcel(self, elements):
        self.file_path = filedialog.askopenfilename(title="Select Excel file",
                                                filetypes=(("Excel files", "*.xlsx;*.xlsm;*.xml"), ("All files", "*.*")))

        if self.file_path:
            self.excel_file = pd.ExcelFile(self.file_path)
            elements["automateBtn"]["state"] = "normal"
            self.loadSheet(elements["canvas"], elements["label"])
            hideElement(elements["uploadBtn"])
            elements["canvas"].itemconfig(elements["uploadImg"], state='hidden')
            elements["verifyBtn"].place(
                x=85.0,
                y=335.0,
                width=80.0,
                height=38.0
            )
            elements["deleteBtn"].place(
                x=85.0,
                y=435.0,
                width=80.0,
                height=38.0
            )
            



    def loadSheet(self, canvas, label):
        currentSheet = pd.read_excel(self.excel_file, sheet_name=self.sheetNo)
        excelHeaders = tuple(currentSheet.columns.values)
        canvas.itemconfig(label, text=f"{self.excel_file.sheet_names[self.sheetNo]:^40}")
        # Create a Frame to hold the Treeview and Scrollbar
        self.frame = Frame(canvas)
        self.frame.place(x=255, y=350, width=400, height=155)

        # Create a TreeView widget
        self.treeview = ttk.Treeview(self.frame)

        # Define some columns
        self.treeview["columns"] = excelHeaders
        self.treeview.column("#0", minwidth=0, width=0)

        for header in excelHeaders:
            self.treeview.heading(header, text=header)
            self.treeview.column(header, minwidth=0, width=int(400/len(excelHeaders)))

        for values in currentSheet.values:
            self.treeview.insert("", "end", values=tuple(values))

        # Create a vertical scrollbar
        self.vertscrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.treeview.yview)
        self.vertscrollbar.pack(side="right", fill="y")

        # Create a horizontal scrollbar
        self.horscrollbar = ttk.Scrollbar(self.frame, orient="horizontal", command=self.treeview.xview)
        self.horscrollbar.pack(side="top", fill="x")

        # Pack the TreeView widget with the scrollbar
        self.treeview.pack(side="left", fill="y", expand=True)

        # Configure the TreeView to use the scrollbar
        self.treeview.configure(yscrollcommand=self.vertscrollbar.set)
        self.treeview.configure(xscrollcommand=self.horscrollbar.set)


    def deleteSheet(self, elements):
        self.excel_file = None
        elements["canvas"].itemconfig(elements["label"], text="")
        elements["automateBtn"]["state"] = "disabled"
        self.frame.destroy()
        hideElement(elements["verifyBtn"])
        hideElement(elements["deleteBtn"])
        showElement(elements["uploadBtn"])
        elements["canvas"].itemconfig(elements["uploadImg"], state="normal")  
        
