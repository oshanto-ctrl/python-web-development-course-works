import json
import random
import os

class FileHandler:
    """Handle read/write for JSON files"""
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                json.dump({}, f)
    
    def read(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    
    def write(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

class VocabularyManager:
    def __init__(self, filename="vocabs.json"):
        self.file = FileHandler(filename)
    
    def view_words(self):
        vocab = self.file.read()
        if not vocab:
            print(f"[NO DATA FOUND] Vocabulary empty!")
            return
        for word, details in vocab.items():
            print(f"\nWord: {word}")
            print(f"Meaning:    {details["Meaning"]}")
            print(f"Example:  {details["Example"]}")
    
    def add_word(self, word, meaning, example):
        vocab = self.file.read()
        if word in vocab:
            print(f"[WORD EXISTS] Entered {word} already in vocab.")
            return
        vocab["Word"] = {
            "Meaning": meaning,
            "Example": example,
        }
        self.file.write(vocab)
        print(f"[SUCCESS] New word '{word}' added to vocab.")

    def search_word(self, word):
        vocab = self.file.read()
        if word in vocab:
            print(f"\n Word: {word}")
            print("Meaning: ", vocab[word]["Meaning"])
            print("Example: ", vocab[word]["Example"])
        else:
            print(f"[NOTHING FOUND] {word} not found in vocab!")

    def update_word(self, word, meaning=None, example=None):
        vocab = self.file.read()
        if word not in vocab:
            print(f"[NOT FOUND] Word {word} not exists in vocab.")
            return
        if meaning:
            vocab[word]["Meaning"] = meaning
        if example:
            vocab[word]["Example"] = example
        self.file.write(vocab)
        print(f"[SUCCESS]. Word '{word}' details have been updated.")

    def delete_word(self, word):
        vocab = self.file.read()
        if word not in vocab:
            print(f"[NOTHING FOUND] {word} does not exists in vocab!")
            return
        del vocab[word]
        self.file.write(vocab)
        print(f"[SUCCESS] Word '{word}' was deleted.")

    def quiz(self):
        vocab = self.file.read()
        if not vocab:
            print(f"[QUIZ ERROR] No words to quiz!")
            return
        word = random.choice(list(vocab.keys()))
        meaning = vocab[word]["Meaning"]
        print(f"[Meaning] = {meaning}")
        answer = input("[What's the word?] = ")
        if answer. strip().lower() == word.lower():
            print(f"[CORRECT ANSWER] Well done. You're write about '{answer}'")
        else:
            print(f"[WRONG ANSWER], Correct word was '{word}'. Try again if you want.")
    
    def export_to_text(self, filename="vocabulary.txt"):
        vocab = self.file.read()
        with open(filename, "w") as f:
            for word, details in vocab.items():
                f.write(f"{word}\n")
                f.write(f"Meaning: {details["Meaning"]}")
                f.write(f"Example: {details["Example"]}")
        print(f"[EXPORT SUCCESFUL] to text file.")

# Validation of menu choice input
def get_menu_choice():
    "Get and validate menu choice"
    while True:
        choice = input("Enter choice: ").strip()
        if len(choice) == 1 and choice.isdigit() and "1" <= choice <= "8":
            return choice
        else:
            print("[Invalid Menu Option] Please enter single digit from 1 to 8")
            return



# main function
def main():
    vbm = VocabularyManager()

    while True:
        print("\n---- Vocabulary Management ---")
        print("1. View all words")
        print("2. Add a new word")
        print("3. Search for a new")
        print("4. Update word details")
        print("5. Delete a word")
        print("6. Quiz Mode")
        print("7. Export vocab to a text file")
        print("8. Exit Vocabulary Management System")

        choice = get_menu_choice()       

        if choice == "1":
            # view all words
            print(f"+++ Available words +++")
            vbm.view_words()
        elif choice == "2":
            # add a word
            print(f"+++ Add a word +++")
            word = input("Word: ").strip()
            meaning = input("Meaning: ").strip()
            example = input("Example: ").strip()
            vbm.add_word(word, meaning, example)
        elif choice == "3":
            # search a word
            print(f"+++ Search a word +++")
            vbm.search_word(input("Enter word: ").strip())            
        elif choice == "4":
            # Update word details
            print("+++ Update word details +++")
            word = input("Word: ").strip()
            meaning = input("New meaning (leave empty to skip): ").strip() # added None in param
            example = input("New Example (leave empty to skip)").strip() # added None in param
            vbm.update_word(word, meaning or None, example or None)
        elif choice == "5":
            # delete a word
            vbm.delete_word(input("Word: ").strip())
        elif choice == "6":
            # quiz mode
            vbm.quiz()
        elif choice == "7":
            # export all words and their details to plain text 
            print(f"Export full vocab to text file.[OK?]")
        elif choice == "8":
            print("[Loggin off] Bye from Vocab Management System.")
            break # log off the Vocab Management Systems

# driver
if __name__ == "__main__":
    main()