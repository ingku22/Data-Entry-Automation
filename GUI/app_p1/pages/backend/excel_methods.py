import pandas as pd
from tkinter import ttk, Frame, filedialog

class ExcelHandler: 
    def __init__(self):
        self.excel_file = None
        self.sheetNo = 0
        self.file_path = ""

    def changeSheet(self, adj, canvas, label):
        num_of_sheets = len(self.excel_file.sheet_names)
        if self.sheetNo + adj >= 0 and self.sheetNo + adj < num_of_sheets:
            self.sheetNo += adj
            self.loadSheet(canvas, label)

    def uploadExcel(self, canvas, label, button):
        self.file_path = filedialog.askopenfilename(title="Select Excel file",
                                                filetypes=(("Excel files", "*.xlsx;*.xlsm;*.xml"), ("All files", "*.*")))

        if self.file_path:
            self.excel_file = pd.ExcelFile(self.file_path)
            button["state"] = "normal"
        self.loadSheet(canvas, label)

    def loadSheet(self, canvas, label):
        currentSheet = pd.read_excel(self.excel_file, sheet_name=self.sheetNo)
        excelHeaders = tuple(currentSheet.columns.values)
        canvas.itemconfig(label, text=f"{self.excel_file.sheet_names[self.sheetNo]:^40}")
        # Create a Frame to hold the Treeview and Scrollbar
        frame = Frame(canvas)
        frame.place(x=255, y=350, width=400, height=155)

        # Create a TreeView widget
        treeview = ttk.Treeview(frame)

        # Define some columns
        treeview["columns"] = excelHeaders
        treeview.column("#0", minwidth=0, width=0)

        for header in excelHeaders:
            treeview.heading(header, text=header)
            treeview.column(header, minwidth=0, width=int(400/len(excelHeaders)))

        for values in currentSheet.values:
            treeview.insert("", "end", values=tuple(values))

        # Create a vertical scrollbar
        vertscrollbar = ttk.Scrollbar(frame, orient="vertical", command=treeview.yview)
        vertscrollbar.pack(side="right", fill="y")

        # Create a horizontal scrollbar
        horscrollbar = ttk.Scrollbar(frame, orient="horizontal", command=treeview.xview)
        horscrollbar.pack(side="top", fill="x")

        # Pack the TreeView widget with the scrollbar
        treeview.pack(side="left", fill="y", expand=True)

        # Configure the TreeView to use the scrollbar
        treeview.configure(yscrollcommand=vertscrollbar.set)
        treeview.configure(xscrollcommand=horscrollbar.set)