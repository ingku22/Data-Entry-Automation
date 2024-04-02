# import tkinter as tk
# import random

# def menu_command(item):
#     print("Selected:", item)

# def submenu_command(item):
#     print("Selected submenu:", item)

# def open_new_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("New Window")
#     new_window.minsize(400, 1)  # Set minimum width to 200
#     new_window.maxsize(400, 400)  # Set maximum width to 200

#     frame = tk.Frame(new_window)
#     frame.pack()

#     item_types = ['hype', 'sigma', 'decent', 'mid', 'low af', 'L+cringe+ratio']
#     lorum_ipsum = "Lorum ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

#     label = tk.Label(frame, text='New Window!', font=("Arial", 18), pady=20)
#     label.pack()

#     description = tk.Text(frame, width=200, height=200, font=('Arial', 16), pady=3, fg='grey')
#     description.insert(tk.END, f'This is a {item_types[random.randint(0, 5)]} page. {lorum_ipsum}')
#     description.config(state='disabled')
#     description.pack(expand=True, fill=tk.Y)

# # Create the Tkinter root window
# root = tk.Tk()
# root.title("Main Window")

# # Create a button to open a new window
# button = tk.Button(root, text="Open New Window", command=open_new_window)
# button.pack()

# root.mainloop()
