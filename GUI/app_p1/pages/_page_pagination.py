import tkinter as tk
import random

# Pages
from img2excel import image2excel
from img_crop_labels import img_crop_label
from imgtoexcel import imagetoexcel

class PaginationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pagination Example")
        self.root.geometry('700x550')
        
        self.pages = {'404': self.create_404()}
        self.current_page = 'Home'
        
        self.create_pages()
        self.init_menu()
        self.show_page(self.current_page)
        
    def create_pages(self):
        menu_items = ['Home', "Image to Excel Reader", "Image to Excel Reader +", 
                      "Crop Toolkit and Viewer", "Expanded Crop Toolkit", 
                      "Merchant Onboarding", "Settings"]
        item_types = ['hype', 'sigma', 'decent', 'mid', 'low af', 'L+cringe+ratio']
        lorum_ipsum = "Lorum ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

        for item in menu_items:  # Menu Items existing in the menu
            frame = tk.Frame(self.root, width=200, height=200, bg="white")
            label = tk.Label(frame, text=item, font=("Arial", 18), pady=20)
            label.pack()

            description = tk.Text(frame, width=200, height=200,
                                  font=('Arial', 16), pady=3, fg='grey')
            
            description.insert(tk.END, f'This is a {item_types[random.randint(0, 5)]} page. {lorum_ipsum}')
            description.config(state='disabled')
            description.pack()

            
            self.pages[item] = frame

        # Actual Pages
        self.pages['Image to Excel Reader'] = image2excel(self.root)
        self.pages['Image to Excel Reader +'] = imagetoexcel(self.root)
        self.pages['Crop Toolkit and Viewer'] = img_crop_label(self.root)
        
        # print(f'Pages Created: {list(self.pages.keys())}')

    def create_404(self):
        frame = tk.Frame(self.root, width=200, height=200, bg='white')
        label = tk.Label(frame, text='404 Not Found', font=('Arial', 18), pady=20)
        label.pack
        
    def show_page(self, page_name):
        try:
            print(f'Now Displaying Page: {page_name}')
            self.pages[self.current_page].pack_forget()
            self.pages[page_name].pack()
            self.current_page = page_name

        except AttributeError:
            print('Unable to find page')
            self.show_page('404')


    def init_menu(self):
        # Create a menu bar
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # Create top-level menu items
        menu_bar.add_command(label="Home", command=lambda: self.show_page("Home"))

        toolkits_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Automation Toolkits", menu=toolkits_menu)

        toolkits_menu.add_command(label="Image to Excel Reader", command=lambda: self.show_page("Image to Excel Reader"))
        toolkits_menu.add_command(label="Image to Excel Reader +", command=lambda: self.show_page("Image to Excel Reader +"))

        cropping_menu = tk.Menu(toolkits_menu, tearoff=0)
        toolkits_menu.add_cascade(label="Category Cropping Toolkit", menu=cropping_menu)
        cropping_menu.add_command(label="Crop Toolkit and Viewer", command=lambda: self.show_page("Crop Toolkit and Viewer"))
        cropping_menu.add_command(label="Expanded Crop Toolkit", command=lambda: self.show_page("Expanded Crop Toolkit"))

        automation_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Automation", menu=automation_menu)

        automation_menu.add_command(label="Merchant Onboarding", command=lambda: self.show_page("Merchant Onboarding"))
        automation_menu.add_command(label="Settings", command=lambda: self.show_page("Settings"))

        menu_bar.add_command(label='Exit', command=exit)
  

if __name__ == "__main__":
    root = tk.Tk()
    app = PaginationApp(root)
    root.mainloop()

