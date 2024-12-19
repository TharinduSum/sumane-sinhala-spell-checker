import os
import re
import unicodedata
import difflib
import tkinter as tk
from tkinter import messagebox

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

# Tokenize text
def tokenize(text):
    words = re.findall(r'\b[\u0D80-\u0DFF]+\b', text)  # Use Unicode range for Sinhala
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

# Load Sinhala text files and prepare dictionary
folder_path = 'sinhala_text_file'
if os.path.exists(folder_path):
    sinhala_corpus = load_sinhala_text_files(folder_path)
    sinhala_words = tokenize(sinhala_corpus)
else:
    sinhala_words = set()
    messagebox.showerror("Error", f"Folder '{folder_path}' not found!")

# GUI Functionality
def check_word():
    entered_word = word_entry.get().strip()
    if not entered_word:
        messagebox.showwarning("Warning", "Please enter a word to check.")
        return

    result = check_spelling(entered_word, sinhala_words)
    result_label.config(text=result)

# Create GUI
root = tk.Tk()
root.title("Sinhala Spell Checker")
root.geometry("500x300")

# Create Input Widgets
tk.Label(root, text="Enter a word to check spelling:", font=("Arial", 14)).pack(pady=10)
word_entry = tk.Entry(root, font=("Arial", 14), width=30)
word_entry.pack(pady=5)

# Check Button
check_button = tk.Button(root, text="Check Spelling", font=("Arial", 14), command=check_word)
check_button.pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 14), fg="green")
result_label.pack(pady=10)

# Run GUI
root.mainloop()
