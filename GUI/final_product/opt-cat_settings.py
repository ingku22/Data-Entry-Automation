import tkinter as tk
from tkinter import ttk

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings")

        self.selection_var = tk.StringVar(value="None")

        # Radiobuttons
        self.none_radio = ttk.Radiobutton(self, text="None", value="None", variable=self.selection_var, command=self.toggle_add_button_state)
        self.include_radio = ttk.Radiobutton(self, text="Only", value="Only", variable=self.selection_var, command=self.toggle_add_button_state)
        self.except_radio = ttk.Radiobutton(self, text="Except", value="Except", variable=self.selection_var, command=self.toggle_add_button_state)

        self.none_radio.grid(row=0, column=0, padx=5, pady=5)
        self.include_radio.grid(row=0, column=1, padx=5, pady=5)
        self.except_radio.grid(row=0, column=2, padx=5, pady=5)

        # Entry and Add Button
        self.entry = ttk.Entry(self)
        self.entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        self.add_button = ttk.Button(self, text="Add", command=self.add_item, state='disabled')
        self.add_button.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        # Listbox
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
        self.listbox.bind('<BackSpace>', self.delete_item)
        self.listbox.bind('<Delete>', self.delete_item)

        # Save Changes Button
        self.save_button = ttk.Button(self, text="Save Changes", command=self.save_changes)
        self.save_button.grid(row=3, column=0, columnspan=3, pady=10)

    def toggle_add_button_state(self):
        if self.selection_var.get() == "None":
            self.add_button.config(state='disabled')
        else:
            self.add_button.config(state='normal')

    def add_item(self):
        text = self.entry.get()
        if text:
            self.listbox.insert(tk.END, text)
            self.entry.delete(0, tk.END)

    def delete_item(self, event):
        selection = self.listbox.curselection()
        if selection:
            self.listbox.delete(selection[0])

    def save_changes(self):
        selected_option = self.selection_var.get()
        items = self.listbox.get(0, tk.END)
        print(f"{selected_option}: {items}")
        self.destroy()

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")

        self.settings_button = ttk.Button(self, text="Settings", command=self.open_settings)
        self.settings_button.pack(padx=10, pady=10)

    def open_settings(self):
        settings_window = SettingsWindow(self)

def main():
    app = MainApplication()
    app.mainloop()

if __name__ == "__main__":
    main()