# imports
from tkinter import ttk


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