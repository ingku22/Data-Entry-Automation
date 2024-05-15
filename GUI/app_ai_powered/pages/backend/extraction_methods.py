from google.cloud import vision 
from google.cloud.vision_v1 import types
import os
import io
import cv2
import pandas as pd

from itertools import combinations as combination
import re

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "TestServiceAccount.json"

def get_text_reading(image_path):
    # Get client
    client = vision.ImageAnnotatorClient()


    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Obtain google vision text readings
    response = client.text_detection(image=image)

    description = []
    for text in response.text_annotations:
        description.append(text.description)

    df = pd.DataFrame({'description': description})
    
    return list(df['description'[1:]])

def Classify(string, col_name, header_name=None):

    if exist_chinese_char(string):
        return 'chinese_text'
    elif string.lstrip().rstrip().lower().replace(' ', '') in get_col_name_combi(col_name):
        return 'null'
    elif is_index(string):
        return 'index'
    elif all_letters(string):
        return 'english_text'
    
    elif is_float(string) or string == '$' or has_numbers(string):
        return 'cost'

    elif has_non_alphanumeric(string):
        return 'null'
    else:
        return 'null'
    
def not_stray_block(string):
    return len(string) > 1

def get_col_name_combi(col_name):
    col_name = [col.lower().replace(' ', '') for col in col_name]
    string_combinations = []
    for length in range(1, len(col_name) + 1):
        combinations = combination(col_name, length)

        string_combinations.extend([''.join(combi) for combi in combinations])

    return string_combinations

def all_letters(string):
        for char in string:
            # Check if the character is within the range of Latin alphabet characters
            if not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122) and char not in list('&/()"'):
                return False
            else:
                return True

def is_float(string):
    try:
        float(string)
        return True
    except:
        return False
    
def has_numbers(string):
    for char in string:
        if char in list('1234567890'):
            return True
        else:
            return False


def exist_chinese_char(string):
    return any('\u4e00' <= char <= '\u9fff' for char in string)

def has_non_alphanumeric(string):
    for char in string:
        if char in list('!@#$%^*+'):
            return True
        else:
            return False

def is_index(string):
    # Check if the string has at least two characters and the last one is a period '.'
    if len(string) >= 2 and string[-1] == '.':
        return True
    # Check if the string is a mix of alphanumerics
    elif string.isalnum() and any(char.isalpha() for char in string) and any(char.isdigit() for char in string):
        return True
    elif len(string) == 1 and 65 <= ord(string) <= 90:
        return True
    return False