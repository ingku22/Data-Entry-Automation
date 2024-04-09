import tkinter as tk
from tkinter import ttk
from settings import SettingsWindow

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        self.category_group_specs = {'specs': "None", 'items': []}
        self.option_groups = ['-(Please select an option)-', 'Option group 1', 'Option group 2', 'Option group 3', 'Local Options']

        self.settings_button = ttk.Button(self, text="Settings", command=self.open_settings)
        self.settings_button.pack(padx=10, pady=10)

        self.specs_label = ttk.Label(self, text="")
        self.specs_label.pack(padx=10, pady=10)

        self.update_specs_label()

    def open_settings(self):
        settings_window = SettingsWindow(self)

    def update_specs_label(self):
        if self.category_group_specs['specs'] != "None" and self.category_group_specs['items'] != ():
            specs_text = f"'{self.category_group_specs['specs']}': {self.category_group_specs['items']}"
            self.specs_label.config(text=specs_text)

        elif self.category_group_specs['items'] == ():
            self.category_group_specs['specs'] = 'None'
        else:
            self.specs_label.config(text="")

        print("Changes saved:", self.category_group_specs)

def main():
    app = MainApplication()
    app.mainloop()

if __name__ == "__main__":
    main()