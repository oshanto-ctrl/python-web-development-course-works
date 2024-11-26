"""
Calculator in python performing basi arithmetic operations
(Addition, Subtraction, Multiplication, Division, Modulo).

User will input and program will perform calcuation and 
handle some basic errors if necessary.
- User input errors.
- Division by zero error.
"""

# Disply menu for user prompting
def display_menu():
    """
    Displays the available operations option to the users.
    
    Operations:
    # [+ - * / %] Arithmetic Operations.
    # ANS: Result of last calculation.
    # Exit the program.
    """
    print("\n\tCalculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Divide (/)")
    print("5. Modulo (%)")
    print("6. Exit. Enter 'exit' without inverted comma to exit the calculator.")


# Get numbers input from user
def get_numbers(input_prompt):
    """
    Takes multiple numbers from user input and returns them as list
    of float datatype.
    Before taking user input a display_prompt given to user to choose
    for operation with 'disply_promp' argument.
    """
    while True:
        try:
            user_input = input(input_prompt) # Taking input as a string.
            numbers = [float(x) for x in user_input.split()] # Converting into list by comprehension & split().
            return numbers # Returning the input to the Calculator() function.
        except ValueError:
            print("Oo Oh! Invalid input! Enter number seperated by space.")


# Addition function
def addition(numbers):
    """
    Performs addition on the numbers given as arguments
    and return the result.
    """
    return sum(numbers)

# Subtraction function
def subtraction(numbers):
    """
    Peforms subtraction using two numbers.
    If user input is more than 2 then slicing for handling multiple inputs.
    Subtracting numbers's first element - sum of all other elements. 
    """
    return numbers[0] - sum(numbers[1:])

# Multiplication function
def multiplication(numbers):
    """
    Performs multiplication on the numbers.
    Loop over the list taking as argument
    and then return the result.
    """
    result = 1 # Handling the input 0
    for num in numbers:
        result = result * num
    return result

# Divide function
def divide(numbers):
    """
    Performs division on two numbers.
    Multiple value is not processed.
    Handling division by zero with try/catch block.
    """
    # Check if input numbers only two otherwise return 'none'
    if len(numbers) != 2:
        print("Oo Oh! More than 2 inputs identified for division! Only supports two numbers.")
        return None
    
    # Division by zero error handling
    try:
        return numbers[0] / numbers[1]
    except ZeroDivisionError:
        print("Oo Oh! Unable to divide by zero.")
        return None
    
# Modulo function
def modulo(numbers):
    """
    Perform modulo on two numbers.
    Check if size more than two.
    Check if zero division error.
    """
    # Check if input numbers only two otherwise return 'none'
    if len(numbers) != 2:
        print("Oo Oh! More than 2 inputs identified for modulo! Only supports two numbers.")
        return None

    # Division by zero error handling
    try:
        return numbers[0] % numbers[1]
    except ZeroDivisionError:
        print("Oo Oh! Unable to modulo by zero.")

# Calculator function
def calculator():
    """
    This function is for user prompting and taking the user input
    to do operations.
    last_result variable to store the result of last calculation.
    """
    last_result = None

    while True:
        # prompt user the display menu.
        display_menu()

        select = input("Enter Operation You Want: ").strip()

        if select == "1" or select.lower() == "+":
            # Input numbers
            numbers = get_numbers("Enter numbers for addition (Space Separated.):\t")
            # Send the numbers list to addition function and store the result.
            result = addition(numbers)
        elif select == "2" or select.lower() == "-":
            # Input numbers
            numbers = get_numbers("Enter numbers for subtraction (Space Separated.):\t")
            # Send the numbers list to subtraction function and store the result.
            result = subtraction(numbers)
        elif select == "3" or select.lower() == "*":
            # Input numbers
            numbers = get_numbers("Enter numbers for multiplication (Space Seperated.):\t")
            # Send the numbers list to multiplication function and store the result.
            result = multiplication(numbers)
        elif select == "4" or select.lower() == "/":
            # Input numbers
            numbers = get_numbers("Enter only two numbers to divide. (Space Seperated.):\t")
            # Send the numbers list to divide function and store the result.
            result = divide(numbers)
        elif select == "5" or select.lower == "%":
            # Input numbers
            numbers = input("Enter two numbers for modulus calculation. (Space Seperated.):\t")
            # Send the numbers list to modulo function and store the result.
            result = modulo(numbers)
        elif select == "6" or select.lower() == "exit":
            # Print a nice message if user want to exit
            print("Exiting Calculator. Sorry to see you leave!")
            break
        else:
            print("Oo Oh! Invalid Selection for operation. Please select a valid operation.")
        
        if result is not None:
            print(f"Result: {result}")
            continue # Giving another change to user for calculation after invalid input.

# Driver to run the calculator
calculator()






