import tkinter as tk
from tkinter import ttk

class ProgressBarWindow:
    def __init__(self, parent):
        self.parent = parent
        self.dummy_file = 'image-u074921.jpg'
        self.crop_type = 'Options'
        self.proccesses = ['Obtaining Cropped Image...', f'Detected {self.crop_type}: {self.dummy_file}...',
                              'Booting OCR model...', 'Extracting Image Text...', 
                              'Sorting Outputs...', 'Saving Outputs into Excel file...', 
                              'Finalizing Excel addition...']
        self.prp_state = 0

        self.label_text = tk.StringVar()
        self.label_text.set('Preparing Dependancies...')
        self.label = tk.Label(parent, textvariable=self.label_text, font=('Arial', 9))
        self.label.pack(anchor='w', padx=5, pady=4)

        self.progress = 0
        self.progress_bar = ttk.Progressbar(parent, orient="horizontal", length=240, mode="determinate")
        self.progress_bar.pack(pady=2)

        self.stop_button = tk.Button(parent, text="Stop", command=self.stop_progress)
        self.stop_button.pack(side='right', padx=10, pady=10)

        self.update_progress()

    def update_progress(self):
        if self.progress < 100:
            self.progress += 1
            self.progress_bar['value'] = self.progress

            if self.progress > 10 and self.progress < 95:
                self.label_text.set(self.proccesses[self.prp_state])
                self.prp_state += 1

                if self.prp_state == len(self.proccesses):
                    self.prp_state = 0

            elif self.progress == 95:
                self.label_text.set('Saving Excel File and Statistics...')
            self.parent.after(25, self.update_progress)

        else:
            self.parent.destroy()

    def stop_progress(self):
        self.parent.destroy()

def start_progress_window():
    progress_window = tk.Toplevel(root)
    progress_window.title("Progress Window")
    progress_window.geometry("250x150")
    ProgressBarWindow(progress_window)

def main():
    global root
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("250x100")

    start_button = tk.Button(root, text="Start Progress", command=start_progress_window)
    start_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
