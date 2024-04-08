from pathlib import Path
import pandas as pd
from tkinter import ttk, Frame, filedialog, PhotoImage, Toplevel, Label, Button
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

    def verifyError(self, err_msg, elements):
        popup = Toplevel()
        popup.resizable(False, False)
        popup.title("Error")
        myFrame = Frame(popup)
        myFrame.pack(fill="both", expand=True)

        # Calculate position for centering popup window relative to main window
        window_position_x = elements["canvas"].winfo_rootx() + int(elements["canvas"].winfo_width() / 2 - popup.winfo_reqwidth() / 2 - 100)
        window_position_y = elements["canvas"].winfo_rooty() + int(elements["canvas"].winfo_height() / 2 - popup.winfo_reqheight() / 2)
        
        # Set position for centering popup window
        popup.geometry("+{}+{}".format(window_position_x, window_position_y))
        
        label = Label(popup, text=err_msg)
        label.pack(pady=20, padx=20)
    
        close_button = Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)

    def verifyExcel(self, elements):
        sheet_names = self.excel_file.sheet_names

        # Verify Excel sheet names exists
        format_sheet_names = ["Menu Items", "Linked Category", "Menu Category", "Linked Dish", "Option Groups", "Linked Options", "Options"]
        for name in format_sheet_names:
            if name not in sheet_names:
                err_msg = f"Sheet name : '{name}' not found in Excel File"
                return self.verifyError(err_msg, elements)
            
        # Verify that sheet columns are accurate
        format_columns_names = {
                                "Menu Items": ["ItemID", "Menu Items", "Description", "Costs", "Image"],
                                "Linked Category": ["ItemID", "CategoryID"],
                                "Menu Category": ["CategoryID", "Category"],
                                "Linked Dish": ["ItemID", "GroupID"],
                                "Option Groups": ["GroupID", "GroupName", "DropDown", "Mandatory"],
                                "Linked Options": ["GroupID", "OptionID"],
                                "Options": ["OptionID", "OptionTitle", "OptionVal"]
                                }
        for i in sheet_names:
            sheet = pd.read_excel(self.excel_file, sheet_name=i)
            sheet_columns = sheet.columns
            for name in format_columns_names[i]:
                if name not in sheet_columns:
                    err_msg = f"Column name : '{name}' not found in sheet : '{i}'"
                    return self.verifyError(err_msg, elements)
                    
            # Verify Linked Tables
            if ("Linked" in i):
                match i:
                    case "Linked Category":
                        ref_ItemID = pd.read_excel(self.excel_file, sheet_name="Menu Items")["ItemID"]
                        ref_CategoryID = pd.read_excel(self.excel_file, sheet_name="Menu Category")["CategoryID"]
                        df1 = pd.merge(sheet, ref_ItemID, how="right", on="ItemID")
                        df2 = pd.merge(sheet, ref_CategoryID, how="right", on="CategoryID")
                    case "Linked Dish":
                        ref_ItemID = pd.read_excel(self.excel_file, sheet_name="Menu Items")["ItemID"]
                        ref_GroupID = pd.read_excel(self.excel_file, sheet_name="Option Groups")["GroupID"]
                        df1 = pd.merge(sheet, ref_ItemID,how="right", on="ItemID")
                        df2 = pd.merge(sheet, ref_GroupID, how="right", on="GroupID")
                    case "Linked Options":
                        ref_GroupID = pd.read_excel(self.excel_file, sheet_name="Option Groups")["GroupID"]
                        ref_OptionID = pd.read_excel(self.excel_file, sheet_name="Options")["OptionID"]
                        df1 = pd.merge(sheet, ref_GroupID, how="right", on="GroupID")
                        df2 = pd.merge(sheet, ref_OptionID, how="right", on="OptionID")
                
                # Compare dataframes to see what data is excluded
                common_df = pd.merge(df1, df2, how="inner")
                compare_df = pd.merge(sheet, common_df, how="outer", indicator=True)
                excluded_data = compare_df[compare_df["_merge"]=="left_only"].drop(columns=["_merge"])
                if (not excluded_data.empty):
                    err_msg = f"Redundant data exists in sheet '{i}'. Data: \n\n{excluded_data.to_string(index=False)}" 
                    return self.verifyError(err_msg, elements)
            # Verify the data for each column
            else:
                for column in sheet_columns:
                    data = sheet[column]
                    # Validate columns with numbers
                    if data.dtype == "int64":
                            if (not data[data < 0].empty):
                                err_msg = f"Number cannot be less than 0 in sheet: '{i}'.\nValue: \n{column}\n{data[data < 0].to_string(index=False)}"
                                return self.verifyError(err_msg, elements)
                    # Validate certain columns
                    match column:
                        case "DropDown":
                            excluded_data = []
                            for index, value in data.items():
                                if not isinstance(value, bool) and value != 1 and value != 0:
                                    excluded_data.append(value)
                                if excluded_data:
                                    err_msg = f"Data is in wrong format in sheet: '{i}'.\nValue: \n{column}\n{data[data < 0].to_string(index=False)}"
                                    return self.verifyError(err_msg, elements)

                        case "Mandatory":
                            excluded_data = []
                            for index, value in data.items():
                                if not isinstance(value, bool) and value != 1 and value != 0:
                                    excluded_data.append(value)
                                if excluded_data:
                                    err_msg = f"Data is in wrong format in sheet: '{i}'.\nValue: \n{column}\n{data[data < 0].to_string(index=False)}"
                                    return self.verifyError(err_msg, elements)


                




