import ast
from autocorrect import Speller


def correct_spelling(sentence):
    spell = Speller(lang='en')
    return spell(sentence)

if __name__ == "__main__":
    # Text file containing errors
    with open('Data-Entry-Automation\Preprocesses\menu1 test.txt') as file:
        a = file.read()
        file.close()
        array = ast.literal_eval(a)

    # Test the correction function
    test_sentences = [elem for elem in array]
    for sentence in test_sentences:
        corrected_sentence = correct_spelling(sentence)
        print(f"Original: {sentence}, Corrected: {corrected_sentence}")





