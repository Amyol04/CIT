for i in range(1, 11, 1): 
        print(i , end='') #counts thingz 


for i in range(0,51,2): 
        print(i, end='') # counts to 50 in 2's 

for i in range(20,0,-2):
    print(i , end='') # even numbers from 20 to 0 

### 4 ) ITERATING THROUGH STRINGS AND USING IFS INSIDE THE LOOP

import string 

s = input("gimme a string!")


for charactar in s: 
    if charactar.islower(): 
        print(charactar.upper(), end='')
    elif charactar.upper():
        print(charactar.lower(), end='')


#### reversing a word !! 

word = input("Enter a word: ")

reversed_word = ""

for char in reversed(word):
    reversed_word += char

print("Reversed Word:", reversed_word)

