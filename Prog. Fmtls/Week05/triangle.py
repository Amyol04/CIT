side1 = input("What is side 1? ")
side2 = input("What is side 2? ")
side3 = input("What is side 3 ")

if side1 == side2 == side3: 
    print("This is a equilateral")
elif side1 == side2 or side1 == side3 or side2 == side3: 
    print("this is a isosceles")
else: 
    print("this is a scalene")