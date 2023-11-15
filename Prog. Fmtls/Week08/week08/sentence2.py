### Write a program to read a sentence from the user.

# a. Add code to count and display the number of letters in the sentence. Approach: iterate through
#the string character by character. Use character.isalpha() on each character in turn to
#determine if it is a letter. If so, add 1 to the counter. If not, do nothing. After the loop, print the
#number of letters.

#b. Add code to count and display the number of blanks.
#c. Add code to count the number of vowels.
#d. Add code to count the number of upper case letters. 


import string

s = input('gimme a sentnce ')

letterCount = 0
blankCount = 0
vowelCount = 0 
upperCaseCount = 0 

for char in s: 

    if char.isalpha():
            letterCount += 1
        
        # Count blanks
    if char.isspace():
            blankCount += 1
        
        # Count vowels
    if char.lower() in "aeiou":
            vowelCount += 1
        
        # Count uppercase letters
    if char.isupper():
            upperCaseCount += 1


print(f"The letter count is {letterCount}")
print(f"The blanks coutn is {blankCount}")
print(f"The vowel count is {vowelCount}")
print(f"The upper case coint is {upperCaseCount}")
