# Monday 11th Exam: 9:15 - 11:15

# Conditional Statement
name = "ksdahf"

# Check if 'c', 'u', and 't' are present in the name.
if 'c' in name and 'u' in name and 't' in name:
    discount = 0.15

# For Loops

# Loop through a tuple of numbers
numbers = (2, 3, 4, 5, 'fred', 23, 45, -2, 56)
for x in numbers:
    print(x)

# Loop through characters in a sentence
sentence = "It is Monday!"

for character in sentence:
    # Print alphabetic characters, replace others with '***'
    if character.isalpha():
        print(character)
    else:
        print('***', end='')

# Loop with a range, stepping by 2
for i in range(1, 10, 2):
    print(i, end='')

# Loop 10 times
for i in range(10):
    print(i, end='')

# Loop through different types of items in a tuple
for item in (4, "fred", 4.5):
    print(type(item), item)
print()

# Counting down with a range
for number in range(10, 1, -1):
    print(number, end=' ')
print()

# Counting up
for number in range(3, 100):
    print(number, end=' ')
print()

# Counting up by 2
for number in range(3, 100, 2):
    print(number, end=' ')

# Get the average of a specified number of user-inputted numbers
number = int(input("How many numbers? "))
total = 0

for i in range(number):
    number = float(input("Number >>> "))
    total += number

average = total / number
print(average)

# Another way to get the average, prompting until valid inputs are provided
total = 0

while True:
    try:
        numNums = int(input("How many numbers: "))
        if numNums > 0:
            break
        else:
            print("Please enter a positive integer for the number of numbers.")
    except ValueError:
        print("Whole numbers only, please :D")

for i in range(1, numNums + 1):
    while True:
        try:
            number = float(input(f"Number {i} >>> "))
            total += number
            break
        except ValueError:
            print("Please enter a valid number.")

average = total / numNums
print("Average:", average)

# Loop through characters in a sentence, printing 'x' for 'e', '*' for punctuation, and the character otherwise.
import string

sentence = input("Sentence pls >> ")
for ch in sentence:
    if ch.lower() == 'e':
        print('x')
    elif ch in string.punctuation:
        print('*', end='')
    else:
        print(ch, end='')
