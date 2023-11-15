sentence = input("Enter a sentence: ")

# a. Replace punctuation marks with 'X' and print the modified sentence
modified_sentence_a = ""
for char in sentence:
    if char.isalpha() or char.isspace():
        modified_sentence_a += char
    else:
        modified_sentence_a += 'X'

print("Modified Sentence (punctuation marks changed to 'X'):")
print(modified_sentence_a)

# b. Print uppercase letters as ASCII codes
print("\nUppercase Letters as ASCII codes:")
for char in sentence:
    if char.isupper():
        print(f"{char}: {ord(char)}")
