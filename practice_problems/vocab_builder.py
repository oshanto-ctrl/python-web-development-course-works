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
    print("\t--- ALL WORDS ---")
    for word, details in vocabs.items():
        print(f"\nWord: {word}")
        print(f"Meaning: {details["Meaning"]}")
        print(f"Example: {details["Example"]}")
    print(FORMAT_DASHES)


# Add new word to vocabs with user prompt (Check duplicate)
def add_word():
    # Prompt: Word, Meaning, Example
    print("\t--- Add word ---")
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
    print("\t--- Search Word ---")
    query_word = input("Enter word to search for: ").strip().lower().replace(" ", "")
    word_found = False

    for word, details in vocabs.items():
        sanitized_word = word.lower().replace(" ", "")

        if query_word == sanitized_word:
            print(f"Word Found\n{'-'*20}")
            print(f"\nWord: {word}")
            print(f"Meaning: {details["Meaning"]}")
            print(f"Example: {details["Example"]}")
            word_found = True
            break
        
    if not word_found:
        print(f"Word '{query_word}' not found.")


# Update existing word details by user prompt
def update_word():
    print("\t--- Search Word ---")
    query_word = input("Enter word to search for: ").strip().lower().replace(" ", "")
    word_found = False

    for word in vocabs:
        sanitized_word = word.lower().replace(" ", "")
        if query_word == sanitized_word:
            word_found = True
            matched_word = word # Storing the found word
            break
    
    if word_found:
        new_meaning = input(f"Enter a new meaning for '{query_word.title()}': ").strip()
        new_example = input(f"Enter a new example '{query_word.title()}': ").strip()
        # Update the new meaning, example
        vocabs[matched_word]['Meaning'] = new_meaning
        vocabs[matched_word]['Example'] = new_example
    else:
        print(f"Query '{query_word}' wasn't found.")
        exit()
    
    # Save to json file
    with open('vocabs.json', 'w') as file:
        json.dump(vocabs, file, indent=4)
    
    print(f"{query_word.title()}'s Meaning and Example updated successfully.")



# Delete a existing word
def delete_word():
    print("\t--- Delete Word ---")
    query_word = input("Enter word you want to delete: ").strip().lower().replace(" ", "")
    query_word_found = False

    for word in list(vocabs):
        normalized_word = word.lower().replace(" ", "")

        if query_word == normalized_word:
            is_confirm = input("Are you sure you want to delete? (yes/no)").strip() 
            if is_confirm.lower() == 'yes':
                del vocabs[word] # Deleted Word
                print(f"Word {query_word.title()} has been deleted successfully!")
            else:
                print(f"Deletion of '{query_word.title()}' was unsuccessful.")
            query_word_found = True
            break
    
    if not query_word_found:
            print(f"Word '{query_word.title()}' Not Found.")
    # save to json
    with open('vocabs.json', 'w') as file:
        json.dump(vocabs, file, indent=4)
    print("JSON Was Updated After Deletion Process.")


# Quiz mode for users(Shuffle and randomness: Check requirement: test2.dox)
def quiz_mode():
    pass


# Export all word to text file (Vocabs.txt)
def export_words():
    try:
        with open("vocabs.txt", "w") as text:
            for word, details in vocabs.items():
                text.write(f"Word: {word}\n")
                text.write(f"Meaning: {details.get('Meaning', 'NULL')}\n")
                text.write(f"Example: {details.get('Example', 'NULL')}\n")
                text.write("\n")
        print("Vocabulary has been succesfully exported to vocabs.txt file.")

    except FileNotFoundError:
        print("'Vocabs.json' file not found!")
    except Exception as e:
        print(f"Encountered Unexpected Error {e}")


# Driver
# all_words()
# add_word()
# search_word()
# update_word()
# delete_word()
export_words()