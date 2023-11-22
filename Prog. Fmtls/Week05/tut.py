# Conditions, Relational Operators, Simple If, Two-Way If/Else

# Logical Operators

# AND
number = int(input("Pick a number"))

# Note: Using logical operators (AND) to check if the number is positive and even.

if number > 0 and number % 2 == 0:
    print(f"Accepted")
else:
    print("Rejected")

# Cards
suit = input("What is the suit?").lower()

# Note: Using logical operators (OR) to check the color of the suit.

if suit == "hearts" or suit == "diamonds":
    print('Red')
elif suit == "spades" or suit == "clubs":
    print('Black')
else:
    print("Invalid suit")

# Boolean: Eligibility
is_eligible = False

grade = int(input("What is your grade?"))

# Note: Using logical operators (AND) to check the grade and providing feedback.

if 70 <= grade <= 100:
    print("Outstanding")
elif 40 <= grade <= 69:
    print("Compliment")
else:
    print("You suck")

# Find the largest of three numbers
a = int(input("Pick number a"))
b = int(input("Pick number b"))
c = int(input("Pick number c"))

# Note: Using logical operators to find the largest number.

if a > b and b > c:
    print("a is larger than b or c")
elif b > a and b > c:
    print("b is bigger")
elif a < c > b:
    print("c is bigger")

# Cake & Money Exercise
how_much = float(input('How much money do you have?'))
like = input('Do you like cake').lower()

# Note: Using logical operators (AND, OR) to decide whether to buy cake.

if how_much >= 5 and like == "yes":
    print('Buy our cake')
elif how_much >= 5 and like == "no":
    print('Buy something else from us')
elif how_much < 5 and like == "yes":
    print('You're too broke, sorry')
elif how_much < 5 and like == "no":
    print('Not interested then')

# Strings
s = "TIS FUKIN WIMDY"
print(s.upper())
print(s.isupper())
print(s[0].isdigit)  # [0] only examines the 1st character to see if it is a digit [also includes {spaces} ]
print(s.startswith("TIS"))

# Tuple - Collection of values
tuple_options = ("It", "Friend", "Mouse")
print(s.startswith(tuple_options))

name1 = "Mary"
name2 = "Mark"

# Note: Using relational operators to compare names.

print(name1 > name2)
print(len(s))  # Prints how many characters are in the string

# Exercise
# 8 characters long & must start with an S
length = 8
first_letter = ('S', 's')
employee_id = input("What is your ID?")

# Note: Checking the validity of an employee ID based on length and starting letter.

if len(employee_id) == length and employee_id.startswith(first_letter):
    print('Valid Employee ID')
else:
    print('Invalid Employee ID')
