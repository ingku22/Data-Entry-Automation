# Imports
import pandas as pd
import re
import openpyxl

# Functions
def format_to_excel(text_chunk):
    items_df, option_grps_df, options_df = convert_text(text_chunk)

    # Get statistics for converted Excel
    stats = {
        'Category': len(set(items_df['Category'])),
        'Menu Items': len(items_df['Menu Item']),
        'Option Groups': len(option_grps_df['Option Groups']),
        'Options': len(options_df['Option'])
    }

    # Get columns of each table
    columns = {
        "Items": ["Category", "Menu Item", "Description", "Costs", "Option Groups"],
        "Option Group": ["Option Groups", "Single", "Mandatory"],
        "Options": ["Option Group", "Option", "Cost"]
    }

    # Get data of each table
    zipped_items = zip(items_df['Category'], items_df['Menu Item'], 
                       items_df['Description'], items_df['Costs'],
                       [', '.join(groups) for groups in items_df['Option Groups']])
    
    zipped_grps = zip(option_grps_df['Option Groups'], option_grps_df['Single'],
                      option_grps_df['Mandatory'])
    
    zipped_options = zip(options_df['Option Group'], options_df['Option'],
                         options_df['Cost'])
    

    data = {'Items': [list(item) for item in zipped_items], 
            'Option Group': [list(grp) for grp in zipped_grps], 
            'Options': [list(opt) for opt in zipped_options]}

    return data, columns, stats

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
            category_match = re.search(r'!(.*?)\s*(\(|\[|$)', each_line)

            if category_match:
                current_group['name'] = category_match.group(1)
                current_group['type'] = 'Items'

                # Get Group Option Links
                optlink_match = re.search(r'\((.*?)\)', each_line)
                option_links = [optlink_match.group(1).strip().split(',') if optlink_match else None][0]

                # Check if group is a multicost group
                colname_match = re.search(r'\[(.*?)\]', each_line)
                column_name = [colname_match.group(1).strip().split(',') if colname_match else None][0]

            else:
                current_group = {'name': None, 'type': None}
                option_links = column_name = None
                print('Group is undefined')
                


        elif each_line[0] == '?': # define option group
            option_grp_match = re.search(r'\?(\w+(?:\s+\w+)*)', each_line)
            grp_settings_match = re.search(r'\((.*?)\)', each_line)

            

            if option_grp_match:
                option_group = option_grp_match.group(1)

                current_group['name'] = option_group
                current_group['type'] = 'Options'
                option_links = None

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
                    items_df['Option Groups'].append(option_links + option_groups)

                elif option_links:
                    items_df['Option Groups'].append(option_links)

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


    # print('Items:',items_df)
    # print('\nOption Groups:', option_grps_df)
    # print('\nOptions:', options_df)

    return items_df, option_grps_df, options_df





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



# with open('test.txt') as test:
#     test_text = test.read()

#     format_to_excel(test_text)