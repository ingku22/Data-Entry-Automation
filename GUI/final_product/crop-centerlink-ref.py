import tkinter as tk
import networkx as nx

class Point:
    def __init__(self, canvas, name, x, y, shape):
        self.canvas = canvas
        self.name = name
        self.x = x
        self.y = y
        self.shape = shape
        self.circle = None
        self.text = None
        self.connected_points = set()  # Set to store connected points
        
        if shape == 'cluster':
            self.circle = self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, outline='blue', fill='light blue')
        elif shape == 'detail':
            self.circle = self.canvas.create_polygon(x, y - 5, x + 5, y + 5, x - 5, y + 5, outline='green', fill='light green')
        
        self.text = self.canvas.create_text(x, y + 10, text=name, fill='black')

class ImageCropper:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Cropper")

        self.canvas = tk.Canvas(master, bg="white", width=500, height=500)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.confirm_button = tk.Button(master, text="Confirm", command=self.confirm_crop)
        self.confirm_button.pack()
        
        self.link_button = tk.Button(master, text="Link Crops", command=self.toggle_link_mode)
        self.link_button.pack()

        self.extract_button = tk.Button(master, text="Extract Structure", command=self.extract_structure)
        self.extract_button.pack()
        
        self.analyse_button = tk.Button(master, text="Analyse Connection", command=self.analyse_connection)
        self.analyse_button.pack()

        self.link_mode = False
        self.rect_start = None
        self.rect_end = None
        self.rect = None
        self.conf_rects = []  # List to store all confirmed rectangles
        self.points = []  # List to store all points (clusters and details)
        self.line = None  # Line for connecting points
        self.start_point = None  # Start point for drawing line

        self.center_shape = tk.StringVar()
        self.center_shape.set("cluster")

        self.cluster_radio = tk.Radiobutton(master, text="Clusters", variable=self.center_shape, value="cluster")
        self.cluster_radio.pack(anchor=tk.W)
        self.detail_radio = tk.Radiobutton(master, text="Details", variable=self.center_shape, value="detail")
        self.detail_radio.pack(anchor=tk.W)

        self.canvas.bind("<ButtonPress-1>", self.start_crop)
        self.canvas.bind("<B1-Motion>", self.draw_rectangle)
        self.canvas.bind("<ButtonRelease-1>", self.end_crop)

    def start_crop(self, event):
        if not self.link_mode:
            self.rect_start = (event.x, event.y)

    def draw_rectangle(self, event):
        if not self.link_mode and self.rect:
            self.canvas.delete(self.rect)
        if not self.link_mode:
            x0, y0 = self.rect_start
            x1, y1 = event.x, event.y
            self.rect = self.canvas.create_rectangle(x0, y0, x1, y1, outline="yellow")

    def end_crop(self, event):
        if not self.link_mode:
            self.rect_end = (event.x, event.y)

    def confirm_crop(self):
        if not self.link_mode and self.rect_start and self.rect_end:
            x0, y0 = self.rect_start
            x1, y1 = self.rect_end
            center_x = (x0 + x1) // 2
            center_y = (y0 + y1) // 2
            shape = self.center_shape.get()
            point_name = f"{shape.capitalize()} {len(self.points) + 1}"
            point = Point(self.canvas, point_name, center_x, center_y, shape)
            self.points.append(point)
            self.conf_rects.append((x0, y0, x1, y1))  # Save crop boundaries
            conf_rect = self.canvas.create_rectangle(x0, y0, x1, y1, outline="green")  # Draw confirmed crop boundaries
            self.rect_start = None
            self.rect_end = None
            self.canvas.delete(self.rect)
            self.conf_rects.append(conf_rect)
            self.rect = None

    def click(self, event):
        if self.link_mode:
            for point in self.points:
                if event.x >= point.x - 5 and event.x <= point.x + 5 and event.y >= point.y - 5 and event.y <= point.y + 5:
                    if self.start_point is None:
                        self.start_point = point
                        self.canvas.itemconfig(self.start_point.circle, fill='red')  # Change color of the previously selected point back to red

                    elif self.start_point != point:
                        self.canvas.itemconfig(point.circle, fill='red')  # Change point color to red
                        self.draw_line(self.start_point, point)
                        self.start_point = None
                    break
        else:
            for point in self.points:
                if event.x >= point.x - 5 and event.x <= point.x + 5 and event.y >= point.y - 5 and event.y <= point.y + 5:
                    self.start_point = point
                    break

    def draw_line(self, point1, point2):
        self.line = self.canvas.create_line(point1.x, point1.y, point2.x, point2.y, fill='red')
        point1.connected_points.add(point2)
        print(f"{point1.name} - {point2.name}")  # Print connected points

    def toggle_link_mode(self):
        self.link_mode = not self.link_mode
        if self.link_mode:
            self.confirm_button.config(state=tk.DISABLED)
            self.canvas.unbind("<ButtonPress-1>")
            self.canvas.unbind("<B1-Motion>")
            self.canvas.unbind("<ButtonRelease-1>")
            self.canvas.bind("<Button-1>", self.click)
        else:
            self.confirm_button.config(state=tk.NORMAL)
            self.canvas.unbind("<Button-1>")
            self.canvas.bind("<ButtonPress-1>", self.start_crop)
            self.canvas.bind("<B1-Motion>", self.draw_rectangle)
            self.canvas.bind("<ButtonRelease-1>", self.end_crop)

    def extract_structure(self):
        with open('lines.txt', 'w') as f:
            for point in self.points:
                for connected_point in point.connected_points:
                    if point.shape == 'cluster' and connected_point.shape == 'detail':
                        f.write(f"{point.name} -> {connected_point.name} (full)\n")
                    elif point.shape == 'cluster' and connected_point.shape == 'cluster':
                        new_cluster_name = f"{point.name}/{connected_point.name}"
                        f.write(f"{point.name} -> {connected_point.name} (merge) = {new_cluster_name}\n")
                    elif point.shape == 'detail' and connected_point.shape == 'cluster':
                        f.write(f"{point.name} -> {connected_point.name} (full)\n")

    def analyse_connection(self):
        G = nx.Graph()
        for point in self.points:
            for connected_point in point.connected_points:
                G.add_edge(point.name, connected_point.name)

        connected_components = list(nx.connected_components(G))
        print("Connected Components:")
        for idx, component in enumerate(connected_components, 1):
            print(f"Component {idx}: {', '.join(component)}")
            

def main():
    root = tk.Tk()
    app = ImageCropper(root)
    root.mainloop()

if __name__ == "__main__":
    main()