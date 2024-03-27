# Imports
# import pandas as pd
from tkinter import messagebox
from tkinter.ttk import Treeview

# Excel Methods
def select_sheet():
    excel_sheets = ['Menu Items', 'Linked Dish', 'Option Groups',
                    'Linked Options', 'Options'] # As of version 2.1
    pass

def obtain_sheet():
    pass

def export_excel():
    pass

# Treeview (datatable) Methods
def tree_add_data(data:list, table, no_null_allowed=True):
    # Reject if not all options filled
    if ((None or '') in data) and no_null_allowed: 
        messagebox.showwarning(title='DepreciationWarning', 
                               message='There seems to be a null value in the form. Please ensure all necessary rows are filled up.')
    else:
        try:
            table.insert(parent='', index='end', value=data)
        except:
            messagebox.showerror(title='PostError',
                                 message='The form you have tried to submit is not compatible with the system.')
            

def tree_remove_data(row_specs, table):
    return 

def tree_remove_all_data(table):
    if type(table) != Treeview:
        pass
    else:
        table.delete(*table.get_children())
