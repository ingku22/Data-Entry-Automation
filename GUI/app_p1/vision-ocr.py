import tkinter as tk
from tkinter import filedialog
from google.cloud import vision

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")

    for text in texts:
        print(f'\n"{text.description}"')

        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
        ]

        print("bounds: {}".format(",".join(vertices)))

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

def select_image():
    path = filedialog.askopenfilename()
    if path:
        detect_text(path)

# Create Tkinter window
root = tk.Tk()
root.title("Text Detection with Google Cloud Vision")

# Add a button to select image
button = tk.Button(root, text="Select Image", command=select_image)
button.pack(pady=20)

root.mainloop()
