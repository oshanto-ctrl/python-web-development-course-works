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


# Add a new case
def add_case():
    # User's input of Case ID, Title, Suspects(list), status
    case_id = input("Enter Case ID: ").strip()
    case_title = input("Enter Title: ").strip()
    case_suspects = input("Enter suspects (Comma between two suspects): ").strip()
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

# Update Case Status
def update_status():
    valid_statuses = ["Open", "Under Investigation", "Closed"]
    # Prompt User
    case_id = input("Enter Case ID: ").strip()
    new_status = input("Enter New Status (Open, Under Investigation, Closed): ").strip()

    # Check for invalid new status
    if new_status not in valid_statuses:
        print("Invalid Status. Please Choose from Open, Under Investigation, or Closed.")
        exit()
    
    # Update status if case exists already
    if case_id in cases:
        cases[case_id]["Status"] = new_status

        with open("cases.json", 'w') as file:
            json.dump(cases, file, indent=4)
        
        print(f"Case ID {case_id} status updated to '{new_status}'")
    else:
        print(f"Case ID '{case_id}' not found.")


# Update Suspects to cases
def update_suspects():
    case_id = input("Enter Case ID to add susptects: ").strip()
    if case_id not in cases:
        print(f"Case ID: {case_id} not found!")
        exit()
    
    new_suspects = input("Enter suspect names to add (Use comma between names): ").strip()
    new_suspects_list = [suspect.strip() for suspect in new_suspects.split(",") if suspect.strip()]
    
    existing_suspects = set(cases[case_id].get("Suspects", []))
    updated_suspects = list(existing_suspects.union(new_suspects_list))

    # Update json file
    cases[case_id]["Suspects"] = updated_suspects

    # Save the file
    with open("cases.json", 'w') as file:
        json.dump(cases, file, indent=4)
    print(f"Supsects updated to case {case_id}")
    print("Updated suspects list:")
    for suspect in updated_suspects:
        print(f"-   {suspect}")

# Drivers
# retrive_cases()
# add_case()
# update_status()
update_suspects()