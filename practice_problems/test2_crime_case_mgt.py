import json

# Open the cases file and load it to cases variable
with open('cases.json', 'r') as file:
    cases = json.load(file)

# Check loaded cases
print(cases)
