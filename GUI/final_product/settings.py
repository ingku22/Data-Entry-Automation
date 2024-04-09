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