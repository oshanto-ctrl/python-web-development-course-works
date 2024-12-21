'''
Exception: If error occurs in you program, an exception is raised and a 
traceback message appears. Traceback message indicates the location and the
type of error that occured.
'''
# Try to divide a number by zero (0)
number = 10
try:
    output = number / 0
except ZeroDivisionError as e:
    print("Error reason: ", e)
    print("You can not divide a number by zero.")

# If no errors occured then the code in except block is ignored.
print("-------------------")

# raise and exception.
name = "ziszas"
try:
    if 'g' in name:
        print("TOP G.")
    else:
        raise ValueError("Computer says Bottom G.")
except ValueError as e:
    print(f"Caught an error: {e}")

name = "ziszas"

# finally block still runs after the try-except block completes.
try:
    if 'g' in name:
        print("TOP G.")
    else:
        raise ValueError("Computer says Bottom G.")
except ValueError as e:
    print(f"Caught an error: {e}")

finally:
    print("Finally block executed")

