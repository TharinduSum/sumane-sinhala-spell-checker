import os
import re
import unicodedata
import difflib

# Function to load text files
def load_sinhala_text_files(folder_path):
    corpus = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), encoding='utf-8') as file:
                corpus += file.read() + " "
    return corpus

# Normalize Sinhala text
def normalize_text(text):
    return unicodedata.normalize('NFC', text)

# Tokenize text and use Unicode range for Sinhala
def tokenize(text):
    words = re.findall(r'\b[\u0D80-\u0DFF]+\b', text)  
    return {normalize_text(word) for word in words}

# Spell check function
def check_spelling(word, dictionary):
    word = normalize_text(word.strip())
    if word in dictionary:
        return f"The word '{word}' is correctly spelled."
    else:
        suggestions = difflib.get_close_matches(word, dictionary, n=5, cutoff=0.8)
        if suggestions:
            return f"Did you mean: {', '.join(suggestions)}?"
        else:
            return "No suggestions found. Please check the word."

# Advanced spell check for sentences
def advanced_spell_check(sentence: str) -> str:
    words = sentence.split()
    corrected_words = []
    for word in words:
        word = normalize_text(word)
        if word in sinhala_words:
            corrected_words.append(word)
        else:
            suggestions = difflib.get_close_matches(word, sinhala_words, n=1, cutoff=0.8)
            corrected_words.append(suggestions[0] if suggestions else word)
    
    return " ".join(corrected_words)



# Load Sinhala text files and prepare dictionary
folder_path = 'sinhala_text_file' 
if os.path.exists(folder_path):
    print("Loading Sinhala text files...")
    sinhala_corpus = load_sinhala_text_files(folder_path)
    sinhala_words = tokenize(sinhala_corpus)
    print(f"Loaded {len(sinhala_words)} unique Sinhala words.")
else:
    sinhala_words = set()
    print(f"Error: Folder '{folder_path}' not found!")
    exit(1)

# Execute spell check once
if __name__ == "__main__":
    print("\nSinhala Spell Checker")
    user_input = input("Enter a Sinhala word or sentence: ").strip()

    if not user_input:
        print("No input provided. Exiting.")
    else:
        if len(user_input.split()) == 1: 
            result = check_spelling(user_input, sinhala_words)
        else:  
            result = advanced_spell_check(user_input)
        
        print("\n=== Results ===")
        print(f"Input: {user_input}")
        print(f"Output: {result}")
    
    print("\nExiting the Spell Checker. Goodbye!")
