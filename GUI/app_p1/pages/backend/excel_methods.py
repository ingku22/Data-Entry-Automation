import os
import json
import openpyxl
from pathlib import Path
import pandas as pd
from tkinter import ttk, Frame, filedialog, PhotoImage, Toplevel, Label, Button

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
    

    def changeSheet(self, adj, canvas, label, x, y, width, height):
        num_of_sheets = len(self.excel_file.sheet_names)
        if self.sheetNo + adj >= 0 and self.sheetNo + adj < num_of_sheets:
            self.sheetNo += adj
            self.loadSheet(canvas, label, x, y, width, height)

    def uploadExcel(self):
        self.file_path = filedialog.askopenfilename(title="Select Excel file",
                                                filetypes=(("Excel files", "*.xlsx;*.xlsm;*.xml"), ("All files", "*.*")))

        if self.file_path:
            self.excel_file = pd.ExcelFile(self.file_path)

    def dataframe_to_excel(self, data, columns):

        if not os.path.isfile("output.xlsx"):
            workbook = openpyxl.Workbook()
            workbook.save("output.xlsx")

        with pd.ExcelWriter("output.xlsx") as writer:
            for sheet_name in columns:
                df = pd.DataFrame(data[sheet_name], columns = columns[sheet_name])
                df.to_excel(writer, sheet_name=sheet_name, index=False)
            
        self.file_path = "output.xlsx"
        self.excel_file = pd.ExcelFile(self.file_path)

    def label_to_excel(menu_name):
        i = 0
        j = 0
        category_data = []
        linkedCategory_data = []
        optionGrp_data = []

        json_path = "GUI/app_p1/assets/staging_dummy/label.json"
        excel_path = "staging_output.xlsx"

        json_file = open(json_path)
        json_data = json.load(json_file)

        if not os.path.isfile(excel_path):
            workbook = openpyxl.Workbook()
            workbook.save(excel_path)

        for category in json_data[menu_name]:
            category_data.append([i, category])
        
            try: 
                option_df = pd.read_excel(excel_path, sheet_name="Option Groups")
            except:
                option_df = []

            for option_grp in json_data[menu_name][category]["option_links"]:
                if len(option_df):
                    if option_grp in option_df["GroupName"].values.tolist():
                        pass
                optionGrp_data.append([j, option_grp])
                linkedCategory_data.append([i, j])
                j += 1
            i += 1

        with pd.ExcelWriter(excel_path) as writer:
            df1 = pd.DataFrame(category_data, columns = ["CategoryID", "Category"])
            df2 = pd.DataFrame(linkedCategory_data, columns=["CategoryID", "GroupID"])
            df3 = pd.DataFrame(optionGrp_data, columns=["GroupID", "GroupName"])
            df1.to_excel(writer, sheet_name="Menu Category", index=False)
            df2.to_excel(writer, sheet_name="Linked Category", index=False)
            df3.to_excel(writer, sheet_name="Option Groups", index=False)



    def loadSheet(self, canvas, label, x, y, width, height):
        # Create a Frame to hold the Treeview and Scrollbar
        self.frame = Frame(canvas)
        self.frame.place(x=x, y=y, width=width, height=height)

        # Create a TreeView widget
        self.treeview = ttk.Treeview(self.frame)

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

        currentSheet = pd.read_excel(self.excel_file, sheet_name=self.sheetNo)
        excelHeaders = tuple(currentSheet.columns.values)
        canvas.itemconfig(label, text=f"{self.excel_file.sheet_names[self.sheetNo]}")

        # Define columns
        self.treeview["columns"] = excelHeaders
        self.treeview.column("#0", minwidth=0, width=0)

        for header in excelHeaders:
            self.treeview.heading(header, text=header)
            self.treeview.column(header, minwidth=0, width=int(400/len(excelHeaders)))

        for values in currentSheet.values:
            self.treeview.insert("", "end", values=tuple(values))
        


    def deleteSheet(self):
        self.excel_file = None
        self.frame.destroy()  

    def verifyExcel(self):
        sheet_names = self.excel_file.sheet_names

        # Verify Excel sheet names exists
        format_sheet_names = ["Menu Items", "Linked Dish", "Option Groups", "Linked Options", "Options"]
        for name in format_sheet_names:
            if name not in sheet_names:
                err_msg = f"Sheet name : '{name}' not found in Excel File"
                return err_msg
            
        # Verify that sheet columns are accurate
        format_columns_names = {
                                "Menu Items": ["ItemID", "Menu Items", "Description", "Costs", "Category"],
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
                    return err_msg
                    
            # Verify Linked Tables
            if ("Linked" in i):
                match i:
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
                    return err_msg
            # Verify the data for each column
            else:
                for column in sheet_columns:
                    data = sheet[column]
                    # Validate columns with numbers
                    if data.dtype == "int64":
                            if (not data[data < 0].empty):
                                err_msg = f"Number cannot be less than 0 in sheet: '{i}'.\nValue: \n{column}\n{data[data < 0].to_string(index=False)}"
                                return err_msg
                    # Validate certain columns
                    match column:
                        case "DropDown":
                            excluded_data = []
                            for index, value in data.items():
                                if not isinstance(value, bool) and value != 1 and value != 0:
                                    excluded_data.append(value)
                                if excluded_data:
                                    err_msg = f"Data is in wrong format in sheet: '{i}'.\nValue: \n{column}\n{data[data < 0].to_string(index=False)}"
                                    return err_msg

                        case "Mandatory":
                            excluded_data = []
                            for index, value in data.items():
                                if not isinstance(value, bool) and value != 1 and value != 0:
                                    excluded_data.append(value)
                                if excluded_data:
                                    err_msg = f"Data is in wrong format in sheet: '{i}'.\nValue: \n{column}\n{data[data < 0].to_string(index=False)}"
                                    return err_msg


                




