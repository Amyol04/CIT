try:
    # Try to execute the following code block
    x = int(input("Enter a number: "))  # Get an integer input for variable x
    y = int(input("Enter another number: "))  # Get another integer input for variable y
    result = x / y  # Attempt to perform division

    # If successful, print the result of the division
    print(f"The result of {x} divided by {y} is: {result}")

except ValueError:
    # If there is a ValueError (e.g., user input is not a valid integer)
    print("Sorry! That was not an integer number. Let's try again!")

except ZeroDivisionError:
    # If there is a ZeroDivisionError (e.g., attempting to divide by zero)
    print("Cannot divide by 0. Please enter a non-zero second number.")

# Notes for College Student:
# - The 'try' block attempts to execute a set of statements that may cause errors.
# - 'ValueError' is caught if the user input is not a valid integer.
# - 'ZeroDivisionError' is caught if the user attempts to divide by zero.
# - Each 'except' block specifies the actions to take if the corresponding error occurs.
# - The 'input' function is used to get user input, and 'int' is used to convert the input to integers.
# - The 'print' statements provide informative messages based on the encountered errors.
