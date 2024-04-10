import json

with open('references/labels_add.json') as json_string:
    data_dict = json.load(json_string)


details_chunk = data_dict['Desserts']['details']
option_links = data_dict['Desserts']['option_links']
local_option_group = details_chunk['local_options']

option_groups = list(option_links.keys())

print(f'Local Option Groups:\n{local_option_group}')
print(f'Option Groups linked to the menu items: {option_groups}')



# crop variable
# staged_image_labels = {}

# crop_detail_chunk = {
#     "coords": [0.114, 0.435, 0.319, 0.726],
#     "details": {
#         "has_header": True,
#         "has_description": False,
#         "max_col": 3,
#         "col_names": ['Small', 'Medium', 'Large'],
#         "local_options": {
#             "Sundae Toppings": {"items": ["No Toppings", "Waffle", "Chocolate Waffle"],
#                             "costs": [0, 3, 4.8]}
#         }
#     },
#     "option_links": {
#         "Ice Cream Flavours": {"specs": "None", "items": []},
#         "Sugar Level": {"specs": "None", "items": []},
#         "Toppings": {"specs": "Exclude", "items": ['Blizzy Sundae', 'Sweet Sweet Sundae', 'Luzon Paradise', 'Tropical Deluxe']},
#         "Sundae Toppings": {"specs": "Only", "items": ['Blizzy Sundae', 'Sweet Sweet Sundae', 'Luzon Paradise', 'Tropical Deluxe']},
#     }
# }

# staged_image_labels['Desserts'] = crop_detail_chunk

# with open('references/labels_add.json', 'w') as labels_container:
#     json.dump(staged_image_labels, labels_container, indent=4)


