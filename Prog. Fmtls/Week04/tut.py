# Week 4 Lecture

# Selection/Conditional Statements
# Exercise - If statement
HOT = 32
COLD = 4
SUN = "\U0000263C"
temp = float(input("What is the temperature"))

# Note: Using conditional statements to check the temperature and provide appropriate feedback.

if temp > HOT:
    print(f"{SUN} It's too hot")
elif temp < COLD:
    print("It's freezing")
else:
    print("It's grand out")

# Comparison Operators: <, <=, !=, >, >=, ==
# Unicode - International standard assigning unique numbers to characters (e.g., snowflake glyph = "\U00002744")
# Boolean - True or False
# \n - New line   \t - Tab

# Exercise 2
number = int(input("Pick a number"))

# Note: Using conditional statements to check if the number is positive, negative, or zero.

if number > 0:
    print("This is a positive number")
elif number < 0:
    print("This is a negative number")
else:
    print("This number is zero")

# Is it a multiple of 10?

# Note: Checking if the number is a multiple of 10.

if number % 10 == 0:
    print(f"{number} is a multiple of 10")
else:
    print("This is not a multiple of 10")

# Is it even?

# Note: Checking if the number is even.

if number % 2 == 0:
    print(f"{number} is even")

# Don't have to use else statements

# Is it odd

# Note: Checking if the number is odd.

if number % 2 != 0:
    print(f"{number} is odd")

# Exercise 3 - Age
age = int(input("What age are you?"))
my_age = 18

# Note: Comparing ages and providing feedback.

if age > my_age:
    print("You are older than me")
elif age < my_age:
    print("You are younger than me")
else:
    print("You are 18")

# Truthy and Falsy
name = input("What is your name?")

# Note: Demonstrating truthy and falsy values with the input name.

if name == "":
    print("That is truthy")  # Non-empty string is truthy
else:
    print("That is falsy")  # Empty string is falsy

# Example - Verification (non-empty)
# While is a loop
while True:
    name = input("What is your name? ")

    # Note: Using a while loop for continuous input until a non-empty name is provided.

    if name:  # More readable if [ if name == "" ]
        print("Please give me something!")
    else:
        break  # Escape from this infinite while loop

# Exercise 4
num = -9

# Note: Demonstrating truthy and falsy values with the number.

if num:
    print("Truthy")
num = 0
if num:
    print("Falsy")  # 0 is Falsy - everything else is Truthy

# Exercise 5
PASS = 40
grade1 = int(input("What is your 1st grade?"))
grade2 = int(input("What is your 2nd grade?"))
grade3 = int(input("What is your 3rd grade?"))

average = (grade1 + grade2 + grade3) / 3

# Note: Calculating average grades and checking if the average is a passing grade.

if average == PASS:
    print(f"You passed with an average of {average:.2f}% ...barely though")
elif average > PASS:
    print(f"You passed with an average of {average:.2f}% ^.^")
else:
    print(f"You failed with an average of {average:.2f} rip")

# Exercise 6
RRP = 10.49
paid = float(input("How much did you pay for the product?"))

# Note: Checking if the paid amount is equal to, greater than, or less than the retail price.

if paid == RRP:
    print(f"You paid the same price as the retail price")
elif paid > RRP:
    overpay = paid - RRP
    print(f"You have paid {overpay} more than the RRP ")
else:
    underpay = (RRP - paid) / RRP
    print(f"You have paid {underpay:.2%} less than the RRP")

# Scope
# print(overpay)  # Can potentially not be used

# Note: Discussing the scope of variables, demonstrating that 'overpay' may not be usable beyond line 106.
# Scope of that variable exists from line 106 -> end of code... may not be created past line 106
