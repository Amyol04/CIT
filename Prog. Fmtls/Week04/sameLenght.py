name = input("enter name 1 ")
name1 = input("enter name 2 ")
# input 

length1= len(name)
length2 = len(name1)
# grabs the lenght of the names 

if length1 == length2:
    print("correct!")

else:
    if length1 > length2:
        difference = length1 - length2
        print(f"{name} is longer than {name1} by {difference} characters.")
    else:
        difference = length2 - length1
        print(f"{name1} is longer than {name} by {difference} characters.")
# 
