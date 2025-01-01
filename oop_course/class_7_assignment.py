'''
Assignment 2

You are tasked with creating a python program for a restaurant that
offers different discounts based on the day and time of the week.
Wreite a python script that prompots the user to input the day of the week
and the time(in 24 hour format) they plan to visit the restaurant.
Based on this information, the program should output the applicable discount offer.

The discount offers are as follows:
# On weekdays (Monday to Friday):
Before 5 PM: No discount.
After 5 PM: 10% discount on the total bill amount.

# On weekends (Saturday and Sunday):
Before 3 PM: 5% discount on the total bill amount.
After 3 PM: 7% discount on the total bill amount.

Your program should validate the user input to ensure it corresponds to valid days of the week
and a valid time format. If the input is invalid, the program should
display an appropriate error message and prompt the user to input again.

Your program should use conditional statements to determine the discount offer
based on the user input.

Ensure your code is well documented and follows python best practices.
'''

def validate_day(day):
    """Validate if the input day is valid."""
    valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    return day.lower() in valid_days

def validate_time(time):
    """Validate if the input time is in correct 24-hour format."""
    try:
        hours = int(time)
        return 0 <= hours <= 23
    except ValueError:
        return False

def get_discount(day, time):
    """Calculate discount based on day and time."""
    day = day.lower()
    time = int(time)
    
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    
    if day in weekdays:
        return 10 if time >= 17 else 0
    else:  # weekend
        return 7 if time >= 15 else 5

def main():
    while True:
        day = input("Enter day of the week: ")
        if not validate_day(day):
            print("Invalid day! Please enter a valid day of the week.")
            continue
            
        time = input("Enter time (24-hour format, 0-23): ")
        if not validate_time(time):
            print("Invalid time! Please enter a valid time in 24-hour format.")
            continue
            
        discount = get_discount(day, time)
        print(f"Your discount is: {discount}%")
        break

if __name__ == "__main__":
    main()