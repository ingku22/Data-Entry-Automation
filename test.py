import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry("400x300")

# Create a Frame to hold the Treeview and Scrollbar
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Create a TreeView widget
treeview = ttk.Treeview(frame)

# Define some columns
treeview["columns"] = ("Name", "Age", "Occupation")

# Add data to the TreeView
treeview.insert("", "end", text="1", values=("John Doe", "30", "Engineer"))
treeview.insert("", "end", text="2", values=("Jane Smith", "25", "Doctor"))
treeview.insert("", "end", text="3", values=("Alice Johnson", "35", "Teacher"))
treeview.insert("", "end", text="4", values=("Bob Brown", "40", "Artist"))
treeview.insert("", "end", text="5", values=("Carol Wilson", "45", "Scientist"))
treeview.insert("", "end", text="6", values=("David Lee", "50", "Manager"))
treeview.insert("", "end", text="7", values=("Emma Taylor", "55", "Developer"))
treeview.insert("", "end", text="1", values=("John Doe", "30", "Engineer"))
treeview.insert("", "end", text="2", values=("Jane Smith", "25", "Doctor"))
treeview.insert("", "end", text="3", values=("Alice Johnson", "35", "Teacher"))
treeview.insert("", "end", text="4", values=("Bob Brown", "40", "Artist"))
treeview.insert("", "end", text="5", values=("Carol Wilson", "45", "Scientist"))
treeview.insert("", "end", text="6", values=("David Lee", "50", "Manager"))
treeview.insert("", "end", text="7", values=("Emma Taylor", "55", "Developer"))
treeview.insert("", "end", text="1", values=("John Doe", "30", "Engineer"))
treeview.insert("", "end", text="2", values=("Jane Smith", "25", "Doctor"))
treeview.insert("", "end", text="3", values=("Alice Johnson", "35", "Teacher"))
treeview.insert("", "end", text="4", values=("Bob Brown", "40", "Artist"))
treeview.insert("", "end", text="5", values=("Carol Wilson", "45", "Scientist"))
treeview.insert("", "end", text="6", values=("David Lee", "50", "Manager"))
treeview.insert("", "end", text="7", values=("Emma Taylor", "55", "Developer"))
treeview.insert("", "end", text="1", values=("John Doe", "30", "Engineer"))
treeview.insert("", "end", text="2", values=("Jane Smith", "25", "Doctor"))
treeview.insert("", "end", text="3", values=("Alice Johnson", "35", "Teacher"))
treeview.insert("", "end", text="4", values=("Bob Brown", "40", "Artist"))
treeview.insert("", "end", text="5", values=("Carol Wilson", "45", "Scientist"))
treeview.insert("", "end", text="6", values=("David Lee", "50", "Manager"))
treeview.insert("", "end", text="7", values=("Emma Taylor", "55", "Developer"))
treeview.insert("", "end", text="1", values=("John Doe", "30", "Engineer"))
treeview.insert("", "end", text="2", values=("Jane Smith", "25", "Doctor"))
treeview.insert("", "end", text="3", values=("Alice Johnson", "35", "Teacher"))
treeview.insert("", "end", text="4", values=("Bob Brown", "40", "Artist"))
treeview.insert("", "end", text="5", values=("Carol Wilson", "45", "Scientist"))
treeview.insert("", "end", text="6", values=("David Lee", "50", "Manager"))
treeview.insert("", "end", text="7", values=("Emma Taylor", "55", "Developer"))

# Set column headings
treeview.heading("#0", text="ID")
treeview.heading("Name", text="Name")
treeview.heading("Age", text="Age")
treeview.heading("Occupation", text="Occupation")

# Create a vertical scrollbar
vertscrollbar = ttk.Scrollbar(frame, orient="vertical", command=treeview.yview)
vertscrollbar.pack(side="right", fill="y")

# Create a vertical scrollbar
horscrollbar = ttk.Scrollbar(frame, orient="horizontal", command=treeview.xview)
horscrollbar.pack(side="top", fill="x")

# Pack the TreeView widget with the scrollbar
treeview.pack(side="right", fill="y")

# Configure the TreeView to use the scrollbar
treeview.configure(yscrollcommand=vertscrollbar.set)
treeview.configure(xscrollcommand=horscrollbar.set)

# Run the Tkinter event loop
root.mainloop()