'''
A program terminates when no more statements exists to execute
in the input program or when an uncaught SystemExit exception is raised.
When we have to force a program to quit, we can use the below methos.
'''
# raise SystemExit()
# raise SystemExit("With Error Message.")

import sys

def main():
    print("Starting program...")
    
    # Simulating some operations
    print("Performing some tasks...")
    
    # Raising SystemExit with a message
    raise SystemExit("An error occurred during program execution.")
    
    # This line won't be reached due to the exception
    print("This won't be printed")

if __name__ == "__main__":
    try:
        main()
    except SystemExit as e:
        print(f"Program exited with error: {str(e)}")




