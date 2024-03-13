from autocorrect import Speller

def correct_spelling(sentence):
    spell = Speller(lang='en')
    return spell(sentence)

if __name__ == "__main__":
    # Test the correction function
    test_sentences = ['helo tis is a senmtance']
    for sentence in test_sentences:
        corrected_sentence = correct_spelling(sentence)
        print(f"Original: {sentence}, Corrected: {corrected_sentence}")