for k in range(5):
 print(k, end=" ")
print()
# OUTPUT: 2 3 4
for i in range(2,5):
 print(i, end=" ")
print()
# OUTPUT: 2 4 6 8 10
for i in range(2, 11,2):
 print(i, end=" ")
print()
#OUTPUT: 11 9 7 5 3 1
for i in range(11, 0, -2):
 print(i, end=" ")
print()
# ITERATING THROUGH A STRING
#OUTPUT:H*e*l*l*o* *W*o*r*l*d*
sentence = "Hello World"
for character in sentence:
 print(character, end="*")