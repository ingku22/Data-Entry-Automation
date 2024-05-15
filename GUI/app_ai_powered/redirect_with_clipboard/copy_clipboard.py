import tkinter as tk

# Function to copy text from the entry widget to the clipboard
def copy_to_clipboard():
    text = entry.get()  # Get text from the entry widget
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(text)  # Append the text to the clipboard
    root.update()  # Now it stays on the clipboard after the window is closed
    feedback_label.config(text="Copied to clipboard!")  # Update feedback label
    entry.delete(0, tk.END)  # Clear the entry widget
    root.after(1500, clear_feedback)  # Clear feedback after 3 seconds

# Function to clear the feedback label
def clear_feedback():
    feedback_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Copy to Clipboard Example")
root.geometry("300x120")  # Set the window size to 400x200 pixels

# Create an entry widget for user input
entry = tk.Entry(root, width=40)
entry.pack(pady=(20, 0))  # Add 20 pixels padding to the top and 10 pixels to the bottom

# Create a button
button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
button.pack(pady=(10, 0))

# Create a feedback label
feedback_label = tk.Label(root, text="")
feedback_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
