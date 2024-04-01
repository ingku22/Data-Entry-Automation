# imports
from tkinter import ttk, messagebox


# dummy data
DEFAULT_COLUMN = ['1', '2', '3']
DEFAULT_DATA = [
    ['apple', 'b', 'c'],
    ['zebra', 'y', 'x'],
    ['whale', 't', 'u']
]


LABEL_COLUMNS = ['Category', 'Cropped Dimensions']
LABEL_DATA = [
    ['Appetizers', '[35,35,35,35]'],
    ['Drinks', '[35,35,35,35]'],
    ['Soups', '[35,35,35,35]'],
    ['Main Dish', '[35,35,35,35]'],
    ['Specials', '[35,35,35,35]']
]

# table methods

# Configure Table Data into ttk.Treeview
def get_ttk_table(root, width=70, column=DEFAULT_COLUMN, data=DEFAULT_DATA, yscroll=False):
    table = ttk.Treeview(master=root, columns=column, show='headings')
     
    for each_column in column:
        table.heading(column=each_column, text=each_column)
        table.column(column=each_column, width=int(width/len(column)))

    for row_data in data:
        table.insert(parent='', index='end', value=row_data)
        

    return table


# Treeview (datatable) Methods
def tree_add_data(data:list, table, no_null_allowed=True):
    # Reject if not all options filled
    if ((None or '') in data) and no_null_allowed: 
        messagebox.showwarning(title='DepreciationWarning', 
                               message='There seems to be a null value in the form. Please ensure all necessary rows are filled up.')
    else:
        try:
            table.insert(parent='', index='end', value=data, )
        except:
            messagebox.showerror(title='PostError',
                                 message='The form you have tried to submit is not compatible with the system.')
            

def tree_remove_data(row_specs, table):
    return 

def tree_remove_all_data(table):
    if type(table) != ttk.Treeview:
        pass
    else:
        children = table.get_children()
        if children:  # Check if there are any children
            # Delete all children except the first one
            table.delete(*children[1:])