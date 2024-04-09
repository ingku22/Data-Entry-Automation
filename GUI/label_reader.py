import json

with open('labels template.json') as json_string:
    data_dict = json.load(json_string)


print(data_dict['image 1']['crop 1.1'])


