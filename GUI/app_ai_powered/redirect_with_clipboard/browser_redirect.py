import tkinter as tk
import webbrowser

# Function to open the web link
def open_link():
    webbrowser.open("https://www.apple.com/")

# Create the main window
root = tk.Tk()
root.title("Open Apple Website")

# Create a button
button = tk.Button(root, text="Open Link", command=open_link)

# Place the button in the window
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()