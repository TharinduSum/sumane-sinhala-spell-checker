import os
import re
import unicodedata
from symspellpy import SymSpell, Verbosity
from indicnlp.tokenize import indic_tokenize
from collections import Counter

sinhala_dictionary_path = r'C:\Users\Ravindu Hasith\Downloads\AI Project\sinhala_dictionary.txt'

# Initialize SymSpell
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=10)

#Clean input word by removing non-Sinhala characters
def clean_input_word(word):
    return re.sub(r'[^඀-෿]', '', word).strip()

#Extract words and their frequencies from a file.
def extract_words_and_frequencies(file_path):
    word_counter = Counter()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = unicodedata.normalize('NFC', line)
                line = re.sub(r'[^඀-෿\s]', '', line)
                tokens = indic_tokenize.trivial_tokenize(line, lang='si')
                words = [word.strip() for word in tokens if re.match(r'^[\u0D80-\u0DFF]+$', word)]
                word_counter.update(words)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    return word_counter

# Load dictionary
print("Loading Sinhala dictionary...")
if os.path.exists(sinhala_dictionary_path):
    word_frequencies = extract_words_and_frequencies(sinhala_dictionary_path)
    for word, freq in word_frequencies.items():
        sym_spell.create_dictionary_entry(word, freq)
    print(f"Total Words in SymSpell Dictionary: {len(sym_spell.words)}")
else:
    print("Sinhala dictionary file not found!")
    exit(1)

def spell_check(word):
    word = clean_input_word(word)
    if not word:
        return word, []

    suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
    if suggestions:
        ranked_suggestions = sorted(suggestions, key=lambda s: (-s.count, len(s.term), s.distance))
        suggested_words = [s.term for s in ranked_suggestions]
        return suggested_words[0], suggested_words
    else:
        return word, []

#Correct a sentence by performing spell checking.
def correct_sentence(sentence):
    words = sentence.split()
    corrected_words = []

    for word in words:
        corrected_word, suggestions = spell_check(word)
        corrected_words.append(corrected_word)

        print(f"Original: {word} | Corrected: {corrected_word} | Suggestions: {suggestions}")

    return " ".join(corrected_words)

if __name__ == "__main__":
    print("\nSinhala Spell Checker")
    user_input = input("Enter a Sinhala sentence: ").strip()
    
    if not user_input:
        print("No input provided. Exiting.")
    else:
        corrected_sentence = correct_sentence(user_input)
        print("\n=== Results ===")
        print(f"Original Sentence: {user_input}")
        print(f"Corrected Sentence: {corrected_sentence}")
    
    print("Exiting Sinhala Spell Checker. Goodbye!")
