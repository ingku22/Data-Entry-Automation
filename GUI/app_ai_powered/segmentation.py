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
    
    current_category = None

    for each_line in cleaned_chunk:
        # -----------------------------------------
        # Check if the format is as stated by the gemini ai prompt results
        # the format of this response should be:
        # Menu Items - costs, costs, costs (Option group)
        # -----------------------------------------
        if each_line.isalpha():
            current_category = each_line 
        elif len(each_line.split(' - ')) <= 2:
            menu_item, item_attr = each_line.split(' - ')[:2]

        elif len(each_line.split(':')) <= 2:
            menu_items, item_attr = each_line.split(':')[:2]

        else:
            menu_items, item_attr = (None, None)
    
    if menu_items and item_attr:
        # ---------------------------
        #  1. Get Menu Items
        # ---------------------------
        items_df['Category'].append(current_category)
        items_df['Menu Item'].append(menu_items)
        items_df['Description'].append('')

        # ------------------------------------------
        # 2. Configure Costs and Option Group
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

        
def clean_text(text_chunk):
    return text_chunk