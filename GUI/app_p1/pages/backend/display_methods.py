from tkinter import HIDDEN

coords = {}

def hideElement(element):
    coords[element] = [element.winfo_x(), element.winfo_y()]
    print(coords[element])
    element.place_forget()

def showElement(element):
    element.place(x=coords[element][0], y=coords[element][1])