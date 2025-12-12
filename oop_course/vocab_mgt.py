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
        pass

    def search_word(self, word):
        pass

    def update_word(self, word, meaning=None, example=None):
        pass

    def delete_word(self, word):
        pass

    def quiz(self):
        pass
    
    def export_to_text(self, filename="vocabulary.txt"):
        pass

# main function
def main():
    pass

# driver
if __name__ == "__main__":
    main()