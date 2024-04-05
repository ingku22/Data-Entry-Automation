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