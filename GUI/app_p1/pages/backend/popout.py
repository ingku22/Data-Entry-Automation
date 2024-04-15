import tkinter as tk

class settings_popout():
    def __init__(self, parent):
        self.parent = parent # to get page class functions
        self.window = tk.Toplevel(parent)

        # Settings variables


        # ======== FRONT END =========
        # windows testing
        self.entry_label = tk.Label(self.window, text='Test:')
        self.entry = tk.Entry(self.window, width=9)
        print("As")

    def get_app_data(self):
        pass

    def get_settings_info(self):
        return self.entry.get()
