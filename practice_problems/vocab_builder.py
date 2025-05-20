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
    # Prompt: Word, Meaning, Example
    new_word = input("Add a new word: ").strip()
    new_meaning = input("Add a new meaning of word: ").strip()
    new_example = input("Add a new example of word: ").strip()

    if new_word not in vocabs:
        vocabs[new_word] = {
            "Meaning": new_meaning,
            "Example": new_example,
        }
    else:
        print(f"Word '{new_word}' already exists!")
        exit()
    # Add to vocabs.json
    with open("vocabs.json", 'w') as file:
        json.dump(vocabs, file, indent=4)
    
    print(f"\nNew word '{new_word}' was successfully added to vocabulary.")


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
# all_words()
add_word()