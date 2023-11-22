# String Operations and Loops

# In Operator
s = "the rain will never stop"

# Note: Using the 'in' operator to check if 'o' is in the string.

if "o" in s:
    print("There is an 'o' in the sentence")

# Vowel Check
letter = 'x'

# Note: Using the 'in' operator to check if the letter is a vowel.

if letter in 'aeiouAEIOU':
    print("Vowel")

# Vowels Tuple
Vowels = 'A', 'E', 'I', 'O', 'U'

# Note: Using the 'in' operator to check if the letter is in the Vowels tuple.

if letter in Vowels:
    print("Vowel")

# String Operations
import string

s = "The rain will never stop"

# Note: Using string operations to check if the letter is lowercase.

print(string.ascii_lowercase)  # Prints lowercase alphabet
print(string.punctuation)  # Prints punctuation characters

# Note: Using string operations to check if the letter is lowercase.

letter = 'x'
if letter in string.ascii_lowercase:
    print("This is lowercase")

# Note: Using string operations to check if the letter is not lowercase.

if letter not in string.ascii_lowercase:
    print("This is not lowercase")

# Memory Check
x = 9
y = 9.0

# Note: Using the 'id' function to check the memory location of variables.

print(id(x))
print(id(y))  # Checks memory location

# Equality Check
print(x == 9)  # Checks if value is the same
print(x is y)  # Checks if they occupy the same memory (Exact same thing)

# Loop - While Loop

# Note: Using a while loop to input names until the user hits ENTER.

names = ""
name = input("Name (ENTER to Quit)  >>>")

while name != "":
    names += name
    name = input("Name (ENTER to Quit)>>>")

print(names)

# Input Number of Names
num_names = int(input("How many do you have?"))
counter = 0

# Note: Using a while loop to input names a certain number of times.

while counter < num_names:
    name = input("Name (Enter to quit) >>>")
    names += name
    counter += 1

print(names)

# While Loop Examples
i = 0

while i < 50:
    print(i)
    i += 1  # Will go from 0 to 49

i = 0

while i > 50:
    print(i)
    i += 1  # 0 Trip. Nothing will happen.

# Looping in 7's
i = 7

while i <= 100:
    print(i)
    i += 7  # Goes up in 7's

# Adding Numbers
total = 0
number = int(input("Number  (0 to quit) >>>"))

while number != 0:
    total += number
    number = int(input("Number  (0 to quit) >>>"))

print(total)

# Copy String with Replacements
s = input("Sentence pls >>>")
i = 0  # Traditional name for the index variable

copy_string = ""
num_char = len(s)  # Number of characters in s

while i < num_char:
    # Note: Using a while loop to make a copy of the string with every vowel replaced with 'x'.
    if s[i] in "AEOIUaeiou":
        copy_string += 'x'
    else:
        copy_string += s[i]
    i += 1

print(copy_string)

# Commission Calculation
com_rate = 0.03
num_sales = int(input("How many sales did you make?"))
counter = 0
total_com = 0

while counter < num_sales:
    sale = float(input("Sale Value >>>"))
    commission = sale * com_rate
    total_com += commission

    print(f"€{sale:.2f} earned you €{commission:.2f} in commission")

    counter += 1

print(output)  # Note: 'output' is not defined; consider using 'print' instead.
print(f"Total earned: €{total_com:.2f}")
