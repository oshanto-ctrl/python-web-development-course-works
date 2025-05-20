import json

# Open the cases file and load it to cases variable
with open('cases.json', 'r') as file:
    cases = json.load(file)

# Check loaded cases
# print(cases)

# Retrieve all the cases
def retrive_cases():
    for case_id, details in cases.items():
        print(f"Case ID: {case_id}")
        print(f"Title: {details['Title']}")
        print(f"Status: {details['Status']}")

        if details['Suspects']:
            print("Suspects:")
            for suspect in details['Suspects']:
                print(f"- {suspect}")
        else:
            print("Suspects: \nFound No Suspects For This Case Currently.")
    
    print("-" * 30)

# Add a new case to json file
def add_case():
    # User's input of Case ID, Title, Suspects(list), status
    case_id = input("Enter Case ID: ").strip()
    case_title = input("Enter Title: ").strip()
    case_suspects = input("Enter suspects (Comma between two suspects)").strip()
    status = input("Enter Case Status (Open/Close): ").strip().capitalize()

    # Make the suspect list
    # suspects = [suspect.strip() for suspect in case_suspects.split(",")] if case_suspects else []
    # if case_suspects:
    #     suspects = [suspect.strip() for suspect in case_suspects]
    # else:
    #     suspects = []
    suspects = [suspect.strip() for suspect in case_suspects.split(",") if suspect.strip()]
    
    # Add the case to json file
    cases[case_id] = {
        "Title": case_title,
        "Suspects": suspects,
        "Status": status
    }

    with open('cases.json', 'w') as file:
        json.dump(cases, file, indent=4)
    
    print(f"Case {case_id} added successfully to Cases.")

# Drivers
retrive_cases()
add_case()
