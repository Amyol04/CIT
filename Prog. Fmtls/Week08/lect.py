#monday 11th exam ! 9.15 - 11.15 

name = "ksdahf"

if 'c' in name and 'u' in name and 't' in name: 
    discount = 0.15 

###

#FOR LOOPPPPS 
 
numbers = (2, 3, 4, 5, 'fred', 23, 45, -2, 56)

for x in numbers: 
    print(x)

##

sentence = "It is Monday!"
# if its a charater, prints character. else ***

for character in sentence: ## char is going to become every character
    if character.isalpha(): #journy though a string 
        print(character)
    else: 
        print('***', end='')

####

for i in range(1, 10, 2): # start at one, end at 10, go up in 2's
        print(1, end='') # when i reaches 10, it stops :D  // jounry though a string. 
    
#####

for i in range(10): # loop 10 times if we neeed to count! 
        print(1, end='')


for item in (4, "fred, 4.5"): 
    print(type(item,), item)
print()

for number in range(10,1, -1):
    print(number, end=' ')
print()

## count down 
##### 

for number in range(3,100):
    print(number, end=' ')
print()

for number in range(3,100,2):
    print(number, end=' ')

#prints all the odd numbers. 
#### 

number = int(input("how many numbers"))
total = 0     
for i in range(number): 
    number = float(input("Number >>>>>>"))
    total += number

average = total / number
print(average)

## asks for an amount of numbers, gets the avrage of the numbers! 

##

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

for i in range(1, numNums +1):
    while True:
        try:
            number = float(input(f"Number {i}>>> "))
            total += number
            break
        except ValueError:
            print("Please enter a valid number.")

average = total / numNums
print("Average:", average)

# User inputs the number of values (`numNums`).
# If a positive integer is entered, the code collects that many numerical inputs.
# Invalid inputs prompt error messages until a valid number is provided.
# The sum of valid numbers is accumulated in the `total` variable.
# The average is calculated by dividing the total by the original number of inputs (`numNums`).
# The calculated average is then displayed as the output.

##### 

import string

sentence = input("Sentence pls >> ")
# print(string.punctuation) // prints string punctuation. 
for ch in sentence: 
    if ch.lower() == 'e': 
        print('x')

    elif ch in string.punctuation:
        print('*', end='')
    
    else: 
        print(ch, end='')

#printing e's as x's
###
