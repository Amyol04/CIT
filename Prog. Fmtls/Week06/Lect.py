

s = "the rain will never stop"

#in operator - is lhs item in lhs item

if "o" in s 
    print("there is an o in the sentence")

letter = x 
if letter in 'aeiouAEIOU':
    print("Vowel")
    
Vowels = 'A','E','I','O','U'

if letter in Vowels:
    print("Vowel")
    
    
######## String

Import string
s = "The rain will never stop"

print(string.ascii_lowercase) # puts into lower case
print(string.punctuation)

letter = x 
if letter in string.ascii_lowercase: 
    print("this is lower case")
    
if letter not in string.ascii_lowercase: 
    print("this is not lower case")
    
####

x = 9
y = 9.0
print(id(x))
print(id(y)) # checks memory! 

print(x == 9) # checks if value is the same.
print(x is y) # checks if they occupy same memory. Exact same thing 

#dont use is , teacher will murder you
 
#### LOOPPPPPS

#names = "" 
#name = input("Name (ENTER to Quit)  >>>")

#names += name # omented operator. 
# same as names = names + name
 
#### While loop

names = "" 
name = input("Name (ENTER to Quit)  >>>")
 while name != "": # as long as the user does not hit ENTER
     names += name
     name = input("Name (ENTER to Quit)>>>")
    
print(names)
 
##

numNames = int(input("How many do you have?")) 
counter = 0
 while counter < numNames: # as long as the user does not hit ENTER
     name = input ("Name (Enter to quit) >>>")
     name += name
     counter += 1
    
print(names)

# get names , make string. 
#####

i = 0

while i < 50:
    print(i)
    i += 1 

# will go from 0 to 49. 

i = 0

while i < 50:
    print(i)
    i -= 1 
    
# will go in -0, ect.. . thete for infante loop

i = 0

while i > 50:
    print(i)
    i += 1 
    
# 0 Trip. Nothing will happen. 

## no do y loop








