# Imports
import pandas as pd
import re
import openpyxl

# Functions
def format_to_excel():
    pass

def convert_text(text_chunk):
    # Needed Variables
    cleaned_chunk = clean_text(text_chunk)

    items_df = {'Category': [], 
                'Menu Item': [],
                'Description': [],
                'Costs': [],
                'Option Groups': []}
    option_grps_df = {'Option Groups': [],
                      'Single': [],
                      'Mandatory': []}
    options_df = {'Option Group': [],
                  'Option': [],
                  'Cost': []}
    
    current_group = {'name': None, 'type': None}

    for each_line in cleaned_chunk:
        if each_line.strip() == '' or len(each_line) < 5:
            pass

        # -----------------------------------------
        # Check if the format is as stated by the gemini ai prompt results
        # the format of this response should be:
        # Menu Items - costs, costs, costs (Option group)
        # -----------------------------------------
        elif each_line[0] == '!': # define category
            # Breakdown category group line into affected option groups and section headers
            category_match = re.search(r'!(\w+(?:\s+\w+)*)', each_line)
            if category_match:
                current_group['name'] = category_match.group(1)
                current_group['type'] = 'Items'
            else:
                current_group = {'name': None, 'type': None}
            


        elif each_line[0] == '?': # define option group
            option_grp_match = re.search(r'\?(\w+(?:\s+\w+)*)', each_line)
            grp_settings_match = re.search(r'\((.*?)\)', each_line)

            

            if option_grp_match:
                option_group = option_grp_match.group(1)

                current_group['name'] = option_group
                current_group['type'] = 'Options'

                if option_group not in option_grps_df['Option Groups'] and grp_settings_match:
                    # find the allocation of option grp settings
                    grp_settings = grp_settings_match.group(1)

                    mandatory = '*' in grp_settings
                    single = '=' not in grp_settings or '-' in grp_settings
                    
                    # Create new option grp if option grp does not exist
                    option_grps_df['Option Groups'].append(option_group)
                    option_grps_df['Single'].append(str(single).upper())
                    option_grps_df['Mandatory'].append(str(mandatory).upper())

                               


        # Split menu items and attributes (costs, option groups)
        # After obtaining the items and item_attr, sorting and data populating can commence
        else:
            items, item_attr = get_items_set(each_line)

            # ------------------------------------------
            # Breaking down items and item_attr
            # based on whether the category is items or options
            # ------------------------------------------
        
            if items and item_attr and current_group['type'] == 'Items':
                # ---------------------------
                # a1. Get Menu Items
                # ---------------------------
                items_df['Category'].append(current_group['name'])
                items_df['Menu Item'].append(items)
                items_df['Description'].append('')

                # ------------------------------------------
                # a2. Configure Costs and Option Group
                # ------------------------------------------
                # Processing the raw item_attr string into individual string
                non_bracket = re.split(r'\(.*?\)', item_attr)
                bracket = re.findall(r'\(.*?\)', item_attr)
                
                non_bracket = [part.strip() for part in non_bracket if part.strip()]
                bracket = [text[1:-1] for text in bracket]

                if len(non_bracket) == 1:
                    costs = non_bracket[0]
                    try:
                        items_df['Costs'].append(float(costs))

                    except:
                        print(f"Cost couldn't be inputtted at: {each_line}")

                if bracket:
                    option_groups = bracket[0].split(',')
                    items_df['Option Groups'].append(option_groups)

                else:
                    items_df['Option Groups'].append([])


            elif items and item_attr and current_group['type'] == 'Options':
                # ---------------------------
                # b. Get Option Groups
                # ---------------------------
                options_df['Option Group'].append(current_group['name'])
                options_df['Option'].append(items)
                try:
                    options_df['Cost'].append(float(item_attr))
                except:
                    options_df['Cost'].append(0)
                    print('Option Cost is not compatible with the cost')


    print('Items:',items_df)
    print('Option Groups:', option_grps_df)
    print('Options:', options_df)





def clean_text(text_chunk):
    return text_chunk.split('\n')


def get_items_set(text_chunk:str):
    if len(text_chunk.split('-')) <= 2:
            items, item_attr = text_chunk.split('-')[:2]

    elif len(text_chunk.split(':')) <= 2:
            items, item_attr = text_chunk.split(':')[:2]

    else:
        items, item_attr = (None, None)

    return items.strip(), item_attr.strip()



with open('test.txt') as test:
    test_text = test.read()

    convert_text(test_text)