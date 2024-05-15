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

        # Point canvas items
        if self.shape == 'Items':
            self.circle = self.canvas.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5, outline='blue', fill='light blue')
        elif self.shape == 'Options':
            self.circle = self.canvas.create_polygon(self.x, self.y - 5, self.x + 5, self.y + 5, self.x - 5, self.y + 5, outline='green', fill='light green')
        
        self.text = self.canvas.create_text(self.x, self.y + 10, text=self.name, fill='red', font=('Arial', 8))

        # Default: hide items
        self.canvas.itemconfig(self.circle, state='hidden')
        self.canvas.itemconfig(self.text, state='hidden')

    def display(self):
        self.canvas.itemconfig(self.circle, state='normal')
        self.canvas.itemconfig(self.text, state='normal')

    def hide(self):
        self.canvas.itemconfig(self.circle, state='hidden')
        self.canvas.itemconfig(self.text, state='hidden')

    def destroy(self):
        self.canvas.delete(self.circle)
        self.canvas.delete(self.text)