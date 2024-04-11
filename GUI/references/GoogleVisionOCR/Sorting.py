import ast

with open('.\\Images\\items.txt', 'r', encoding='utf-8') as raw_list:
    block_list = ast.literal_eval(raw_list.read())


classification = {'Chinese text': [], 'English text': [], 'Price': []}

# Sorting functions
def all_letters(strings):
    for string in strings:
        for char in string:
            # Check if the character is within the range of Latin alphabet characters
            if not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
                return False
    return True

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

classification['Chinese text'].pop(0)
    

output_string = ''
for keys in classification.keys():
    output_string += f'{keys}({len(classification[keys])}): {classification[keys]}\n'

with open('.\\Images\\items(sorted).txt', 'w', encoding='utf-8') as classified_list:
    classified_list.write(output_string)