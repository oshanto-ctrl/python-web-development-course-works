'''
Case management system.
Scenario:
You are creating a program for a police department to manage 
crime cases. The data for each case is stored in a 
file named cases.json in dictionary format.
'''
import json
import os

class FileHandler:
    """Handles file read/write for JSON files"""
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                json.dump({}, f) # create an empty case file
    
    def read(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    
    def write(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)


class CrimeManager:
    """Main class to operate crime cases"""
    def __init__(self, filename="cases.json"):
        self.file =FileHandler(filename) # FileHandler class Object
    
    def view_cases(self):
        cases = self.file.read()
        if not cases:
            print("No cases found.")
            return

        for case_id, details in cases.items():
            print(f"\nCase ID: {case_id}")
            print(f"Title: {details["Title"]}")
            print(f"Suspects:", ", ".join(details["Suspects"]) if details["Suspects"] else "No suspects")
            print(f"Status: {details["Status"]}")

    def add_case(self, case_id, title, suspects, status):
        cases = self.file.read()
        if case_id in cases:
            print("Case id [{case_id}] exists. Want to open?")
            return
        cases[case_id] = {
            "Title": title,
            "Suspects": suspects,
            "Status": status,
        }
        self.file.write(cases)
        print(f"[Success] Case {case_id} added in the Crime Database.")
    
    def update_case_status(self, case_id, status):
        cases = self.file.read()
        if case_id not in cases:
            print(f"[Invalid Case Id] {case_id} wasn't found!")
            return
        cases[case_id]["Status"] = status
        self.file.write(cases) # Enter updated status value
        print(f"[Success] Case status updated for case id: ({case_id})")
    
    def add_case_suspects(self, case_id, new_suspects):
        cases = self.file.read()
        if case_id not in cases:
            print(f"[Invalid Case Id]{case_id} wasn't found!")
            return
        existing_suspects = set(cases[case_id]["Suspects"])
        for suspect in new_suspects:
            existing_suspects.add(suspect)
        cases[case_id]["Suspects"] = list(existing_suspects) # Added as list
        self.file.write(cases)
        print(f"[Success] New suspects were added for case id ({case_id})")
    
    def search_open_cases(self):
        cases = self.file.read()
        for case_id, details in cases.items():
            if details["Status"].lower() == "open":
                print(f"[Success] ({case_id} - Status(OPEN))\nDetails:\n{details["Title"]}")

    def delete_case(self, case_id):
        cases = self.file.read()
        if case_id not  in cases:
            print("[Invalid Case Id] ({case_id}) wasn't Found!")
            return
        del cases[case_id] #    delets case
        self.file.write(cases)
        print(f"[Success] Case ({case_id}) has been delete.")

    def find_cases_by_suspect(self, name):
        cases = self.file.read()
        suspects_found = []
        for case_id, details in cases.items():
            if name in details["Suspects"]:
                suspects_found.append((case_id, details["Title"]))
        if suspects_found:
            print(f"[Success] Case involving {name}")
            for case_id, title in suspects_found:
                print(f"- {title} ({case_id})")
        else:
            print(f"[Unsuccess] No cases found with suspect: {name.title()}")


def get_menu_choice():
    "Get and validate menu choice"
    while True:
        choice = input("Enter choice: ").strip()
        if len(choice) == 1 and choice.isdigit() and "1" <= choice <= "8":
            return choice
        else:
            print("[Invalid Menu Option] Please enter single digit from 1 to 8")
            return

def main():
    cms = CrimeManager()

    while True:
        print("\n---- VCPD Crime Case Management ---")
        print("1. View all cases")
        print("2. Add new case")
        print("3. Update case status")
        print("4. Add suspects")
        print("5. Search open cases")
        print("6. Delete a case")
        print("7. Find cases by suspect")
        print("8. Exit Crime Management System")

        choice = get_menu_choice()       

        if choice == "1":
            # view all cases
            print(f"+++ Available Cases +++")
            cms.view_cases()
        elif choice == "2":
            # add a case
            print(f"+++ Add a Case +++")
            case_id = input("Case ID: ").strip()
            title = input("Case Title: ").strip()
            suspects = input("Suspects (comma-seperated): ").split(",")
            suspects = [s.strip() for s in suspects if s.strip()]
            status = input("Status: ").strip()
            cms.add_case(case_id, title, suspects, status)
        elif choice == "3":
            # update case status
            print(f"+++ Update a Case Status +++")
            case_id = input("Case ID: ").strip()
            status = input("New status: ").strip()
            cms.update_case_status(case_id, status)
        elif choice == "4":
            # Add suspect to list
            print("+++ Add new suspects to selected case +++")
            case_id = input("Case ID: ").strip()
            suspects = input("New suspect (Comma Seperated): ").split(",")
            suspects = [s.strip() for s in suspects if s.strip()]
            cms.add_case_suspects(case_id, suspects)
        
        elif choice == "5":
            # Search open cases 
            print("+++ OPEN CASES +++")
            cms.search_open_cases()
        elif choice == "6":
            # delete a case
            print("+++ Delete a case +++")
            case_id = input("Case ID VCPD wants to delete: ").strip()
            cms.delete_case(case_id)
        elif choice == "7":
            # find case by suspect
            print("+++ Search case by suspect +++")
            suspect = input("Suspect name: ")
            cms.find_cases_by_suspect(suspect)
        elif choice == "8":
            print("[Loggin off] Bye from VCPD Crime Management System.")
            break # log off the Crime Management Systems

if __name__ == "__main__":
    main()  #   Calls the main function



