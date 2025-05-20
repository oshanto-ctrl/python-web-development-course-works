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
            print()
        else:
            print("Suspects: \nFound No Suspects For This Case Currently.\n")
    
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

# Search Cases Status: 'Open'
def search_open_cases():
    print("\nOpen Cases:")
    found = False
    for case_id, details in cases.items():
        if details["Status"].lower() == "open":
            print(f"\nCase ID: {case_id}")
            print(f"Title: {details["Title"]}")
            print(f"Suspects: {', '.join(details["Suspects"]) if details["Suspects"] else "None"}")
            found = True
    if not found:
        print("No Open Cases Found.")


# Delete an existing case.
def delete_case():
    case_id = input("Enter Case ID to Delete: ").strip()
    if case_id in cases:
        confirm = input(f"Are you sure you want to delete case '{case_id}'? (yes/no)").lower()
        if confirm == "yes":
            del cases[case_id]
            print(f"Case '{case_id}' has been deleted.")
        else:
            print("Case Deletion Was Canceled.")
    else:
        print(f"Case ID '{case_id}' not found!")


# Find cases by suspect name
def find_cases_by_suspect():
    suspect_name = input("Enter suspect name: ").strip().lower()
    found = False
    print(f"Case involing suspect {suspect_name}")
    
    for case_id, details in cases.items():
        if any(suspect_name == suspect.lower() for suspect in details['Suspect']):
            print(f"\nCase ID: {case_id}")
            print(f"\nCase Title: {details['Title']}")
            print(f"Status: {details['Status']}")
            print(f"Suspects: {', '.join(details['Suspects'])}")
            found = True

    if not found:
            print(f"No cases involved with {suspect_name}")


# Drivers
# retrive_cases()
# add_case()
# update_status()
# update_suspects()
# search_open_cases
# delete_case()
# find_cases_by_suspect()

while True:
    print(f"\n--- Case Management ---")
    print(f"1. All Cases")
    print(f"2. Search 'OPEN' Cases")
    print(f"3. Find by Suspect Name")
    print(f"4. Add Case")
    print(f"5. Update Suspect List")
    print(f"6. Updated Case Status")
    print(f"7. Delete Case")
    print(f"8. Exit")

    choice = input("Choose and option (1-8): ").strip()

    match choice:
        case "1":
            retrive_cases()
        case "2":
            search_open_cases()
        case "3":
            find_cases_by_suspect()
        case "4":
            add_case()
        case "5":
            update_suspects()
        case "6":
            update_status()
        case "7":
            delete_case()
        case "8":
            print("Exiting program...")
            break
        case _:
            print("Invalid choice. Please select 1-8.")
        