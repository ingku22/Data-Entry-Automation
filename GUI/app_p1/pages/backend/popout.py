import tkinter as tk

class settings_popout():
    def __init__(self, parent, main_app):
        self.parent = parent # to get page class functions
        self.main_app = main_app # tkinter window located in the main page_pagination
        self.window = tk.Toplevel(parent.root)

        # Settings variables


        # ======== FRONT END =========
        # windows testing
        self.entry_label = tk.Label(self.window, text='Test:')
        self.entry = tk.Entry(self.window, width=9)

    def get_app_data(self):
        pass

    def get_settings_info(self):
        return self.entry.get()




