import json
FORMAT_DASHES = "-" * 50
with open("vocabs.json", "r") as file:
    vocabs = json.load(file)

# Print Vocabs
# print(vocabs)
# v = json.dumps(vocabs, indent=2)
# print(v)

# Display all the words in vocabulary
def all_words():
    print("--- ALL WORDS ---")
    for word, details in vocabs.items():
        print(f"\nWord: {word}")
        print(f"Meaning: {details["Meaning"]}")
        print(f"Example: {details["Example"]}")
    print(FORMAT_DASHES)

# Add new word to vocabs with user prompt (Check duplicate)
def add_word():
    pass


# Search a word with user input
def search_word():
    pass


# Update existing word details by user prompt
def update_word():
    pass


# Delete a existing word
def delete_word():
    pass


# Quiz mode for users(Shuffle and randomness: Check requirement: test2.dox)
def quiz_mode():
    pass


# Export all word to text file (Vocabs.txt)
def export_words():
    pass


# Driver
all_words()