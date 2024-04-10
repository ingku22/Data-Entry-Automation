import tkinter as tk
from tkinter import ttk

class SettingsWindow(tk.Toplevel):
    def __init__(self, main_app):
        super().__init__(main_app)
        self.title("Settings")
        self.main_app = main_app

        self.selection_spec = tk.StringVar(value=main_app.category_group_specs['specs'])
        self.selected_option_group = tk.StringVar()

        # Set minimum size of the window
        self.minsize(350, 350)

        # Menu Item Details
        details_label = ttk.Label(self, text="Linked Options Config", font=("Helvetica", 14, "bold"))
        details_label.pack(side="top", padx=10, pady=10, anchor="w")

        # Selected Option Group Label and Option Menu
        option_frame = ttk.Frame(self)
        option_frame.pack(side="top", padx=5, pady=10, fill="x")
        
        option_label = ttk.Label(option_frame, text="Selected Option Group:")
        option_label.pack(side="left", padx=5, pady=5)

        self.option_menu = ttk.OptionMenu(option_frame, self.selected_option_group, *main_app.option_groups, command=self.option_changed)
        self.option_menu.pack(side="left", padx=5, pady=5)


        # Radiobuttons
        radio_frame = ttk.Frame(self)
        radio_frame.pack(side="top", padx=5, pady=5, fill="x")

        none_radio = ttk.Radiobutton(radio_frame, text="None", value='None', variable=self.selection_spec, command=self.toggle_add_button_state)
        include_radio = ttk.Radiobutton(radio_frame, text="Only", value="Only", variable=self.selection_spec, command=self.toggle_add_button_state)
        except_radio = ttk.Radiobutton(radio_frame, text="Exclude", value="Exclude", variable=self.selection_spec, command=self.toggle_add_button_state)

        none_radio.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        include_radio.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        except_radio.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        # Configure columns to expand evenly
        for i in range(3):
            radio_frame.grid_columnconfigure(i, weight=1)

        # Entry and Add Button
        entry_frame = ttk.Frame(self)
        entry_frame.pack(side="top", padx=5, pady=5, fill="x")

        self.entry = ttk.Entry(entry_frame)
        self.entry.pack(side="left", padx=(0, 5), pady=5, fill="x", expand=True)

        self.add_button = ttk.Button(entry_frame, text="Add", command=self.add_item, state='disabled')
        self.add_button.pack(side="left", padx=5, pady=5)

        # Listbox
        self.listbox = tk.Listbox(self)
        self.listbox.pack(side="top", padx=5, pady=5, fill="both", expand=True)
        self.listbox.bind('<BackSpace>', self.delete_item)
        self.listbox.bind('<Delete>', self.delete_item)

        # Save Changes Button
        self.save_button = ttk.Button(self, text="Save Changes", command=self.save_changes)
        self.save_button.pack(side="top", padx=5, pady=10)

        # Initialize listbox with existing items
        for item in main_app.category_group_specs.get('items', []):
            self.listbox.insert(tk.END, item)

    def option_changed(self, selected_option):
        print("Selected Option Group:", selected_option)
        # Add any actions you want to perform when the option group is changed

    def toggle_add_button_state(self):
        if self.selection_spec.get() == "None":
            self.entry.unbind('<Return>')
            self.add_button.config(state='disabled')
            self.listbox.delete(0,'end')
        else:
            self.entry.bind('<Return>', self.add_item)
            self.add_button.config(state='normal')

    def add_item(self, event=None):
        text = self.entry.get()
        if text:
            self.listbox.insert(tk.END, text)
            self.entry.delete(0, tk.END)

    def delete_item(self, event):
        selection = self.listbox.curselection()
        if selection:
            self.listbox.delete(selection[0])

    def save_changes(self):
        selected_option = self.selection_spec.get()
        items = self.listbox.get(0, tk.END)
        self.main_app.category_group_specs['specs'] = selected_option
        self.main_app.category_group_specs['items'] = items
        self.main_app.update_specs_label()
        self.destroy()



class SettingsWindow2(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings 2")
        self.geometry("350x350")  # Set initial window size

        # Create a canvas to contain all the widgets
        canvas = tk.Canvas(self, height=350, width=300)
        canvas.pack(side="left", fill="both", expand=True)

        # Create a frame to contain the widgets inside the canvas
        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        # Add a vertical scrollbar to the canvas
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.config(yscrollcommand=scrollbar.set)

        # Menu Item Details
        details_label = ttk.Label(frame, text="Menu Item Details", font=("Helvetica", 14, "bold"))
        details_label.pack(side="top", padx=10, pady=10, anchor="w")

        # Checklists
        self.has_headers_var = tk.BooleanVar(value=True)
        self.has_descriptions_var = tk.BooleanVar()
        self.columns = []

        has_headers_checkbox = ttk.Checkbutton(frame, text="Has Headers", variable=self.has_headers_var)
        has_headers_checkbox.pack(side="top", padx=10, pady=5, anchor="w")

        has_descriptions_checkbox = ttk.Checkbutton(frame, text="Has Descriptions", variable=self.has_descriptions_var)
        has_descriptions_checkbox.pack(side="top", padx=10, pady=5, anchor="w")

        # Entry widgets and list of column names
        self.entry_frame = tk.Frame(frame, background="#D4D4D4")
        self.entry_frame.pack(side="top", fill="x", padx=10, pady=5)

        max_columns_label = ttk.Label(self.entry_frame, text="Max Columns:", background='#D4D4D4')
        max_columns_label.grid(row=0, column=0, padx=(10, 5), pady=5, sticky="e")

        entry_var = tk.StringVar()
        self.max_columns_entry = ttk.Entry(self.entry_frame, textvariable=entry_var, width=2)
        self.max_columns_entry.grid(row=0, column=1, padx=(0, 5), pady=5, sticky='w')

        entry_var.trace_add("write", lambda *args: self.update_columns_label(entry_var.get()))

        column_names_label = ttk.Label(self.entry_frame, text="Columns:", background='#D4D4D4')
        column_names_label.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="e")

        self.column_names_entry = ttk.Entry(self.entry_frame, width=30)
        self.column_names_entry.grid(row=1, column=1, padx=(0, 10), pady=5, sticky="ew")

        # Local Options
        local_options_label = ttk.Label(frame, text="Local Options", font=("Helvetica", 14, "bold"))
        local_options_label.pack(side="top", padx=10, pady=10, anchor="w")

        # Option, Cost entries, and Add button in a single line
        option_frame = ttk.Frame(frame)
        option_frame.pack(side="top", padx=10, pady=5, fill="x")
        ttk.Label(option_frame, text="Option:").pack(side="left", padx=(5, 2))
        self.option_entry = ttk.Entry(option_frame, width=16)
        self.option_entry.pack(side="left")
        ttk.Label(option_frame, text="Cost:").pack(side="left", padx=(5, 2))
        self.cost_entry = ttk.Entry(option_frame, width=5)
        self.cost_entry.pack(side="left")
        ttk.Button(option_frame, text="Add", command=self.add_local_option).pack(side="left", padx=(2, 0))

        # Treeview for local options
        self.treeview = ttk.Treeview(frame, columns=("option", "cost"), show="headings")
        self.treeview.heading("option", text="Option")
        self.treeview.column("option", width=100)
        self.treeview.heading("cost", text="Cost")
        self.treeview.column("cost", width=100)
        self.treeview.pack(side="top", padx=10, pady=5, fill="both", expand=True)

        # Add Local Option Group
        add_local_options_frame = ttk.Frame(frame)
        add_local_options_frame.pack(side="top", padx=10, pady=5, fill="x")
        ttk.Label(add_local_options_frame, text="Option Group:").pack(side="left", padx=(2, 2))
        self.local_options_name_entry = ttk.Entry(add_local_options_frame, width=20)
        self.local_options_name_entry.pack(side="left")
        ttk.Button(add_local_options_frame, text="Add Local Options").pack(side="left", padx=(2, 0))



        # Update the canvas scroll region when the frame size changes
        frame.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

    def add_column_name(self):
        column_name = self.column_names_entry.get()
        if column_name:
            self.column_names_listbox.insert(tk.END, column_name)
            self.column_names_entry.delete(0, tk.END)

    def add_local_option(self):
        option = self.option_entry.get()
        cost = self.cost_entry.get()
        if option and cost:
            self.treeview.insert("", "end", values=(option, cost))
            self.option_entry.delete(0, tk.END)
            self.cost_entry.delete(0, tk.END)

    def update_columns_label(self, value):
        try:
            num_columns = int(value)
            if num_columns <= 5:
                self.columns = ["opt"] * num_columns

        except ValueError:
            num_columns = 0
            self.columns = ""

        
        self.column_names_entry.delete(0, tk.END)
        self.column_names_entry.insert(0, str(self.columns))