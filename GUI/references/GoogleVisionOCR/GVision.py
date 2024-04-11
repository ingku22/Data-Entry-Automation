# Defeault just print out scanned text & options to output to a file

from google.cloud import vision 
from google.cloud.vision_v1 import types
import os
import io
import cv2
import pandas as pd

import matplotlib.pyplot as plt

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "TestServiceAccount.json"

# FUNCTIONS

def all_letters(strings):
    for string in strings:
        for char in string:
            # Check if the character is within the range of Latin alphabet characters
            if not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
                return False
    return True


def sort_text(block_list):
    classification = {'Chinese text': [], 'English text': [], 'Price': []}

    for block in block_list:
        if any('\u4e00' <= char <= '\u9fff' for char in block) and len(block) > 1:
            classification['Chinese text'].append(block)

        # Check if the block contains prices
        elif '$' in block and len(block) > 1:
            classification['Price'].append(block)

        # Check if the block contains only English characters or a mixture of English and digits
        elif all_letters(block.replace(' ', '')) and len(block) > 1:
            classification['English text'].append(block)

        else:
            pass

    return classification


# MAIN

client = vision.ImageAnnotatorClient()
image_name = 'Menu01'
# image_path = f'.\\staging\\{image_name}'
image_path = f'.\\ExpImg'

output_string = ''

for crops in os.listdir(image_path):
    crop_path = f'{image_path}\\{crops}'

    with io.open(crop_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)  # returns TextAnnotation

    description = []
    bounding_boxes = []

    # Load the image using OpenCV for displaying bounding boxes
    img = cv2.imread(crop_path)
    # height, width, _ = img.shape

    for text in response.text_annotations:
        # Extract the bounding box vertices
        description.append(text.description)
        vertices = [(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices]
        bounding_boxes.append(vertices)

    # Draw bounding boxes on the image
    for vertices in bounding_boxes:
        for i in range(len(vertices)):
            cv2.line(img, vertices[i], vertices[(i + 1) % len(vertices)], (0, 255, 0), 2)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    df = pd.DataFrame({'description': description})
    raw_block_list = df['description'][0].split('\n')

    elements = df['description'][1:]
    for elm in elements:
        output_string += f'(text: en)  {elm}\n' 

    # classified_list = sort_text(raw_block_list)

    # output_string += f'{crops}: \n'

    # for keys in classified_list.keys():
    #     output_string += (f'{keys}({len(classified_list[keys])}): {classified_list[keys]}\n')


with open(f'.\\ExpImg\\output.txt', 'w', encoding='utf-8') as text_collector:
    text_collector.write(output_string)

plt.imshow(img_rgb)
plt.axis('off')
plt.show()