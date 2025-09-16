'''
This code is written to practice the error_handling codes
'''

def handling():
    """Continuously prompt the user for an integer until valid input is received."""
    while True:

        try:
            n1 = int(input("Enter the number: "))

        except ValueError:
            print("This is not the number")

        else:
            print(f"You have entered the number {n1}")
            break

    print("Thank you")


handling()
