alphabet = input("give me a letter from the alphabet")
vowel = ("a","e","i","o","u")


if alphabet.isdigit(): 
    print("Error: try again!")
elif alphabet in "aeiou": 
    print("this contails a vowel")
