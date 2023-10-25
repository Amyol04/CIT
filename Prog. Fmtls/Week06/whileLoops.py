import math

n = int(input("Please enter a number, n: "))
total = 0

for i in range(1, n + 1):
    print("Current number:", i)
    
    square = i ** 2
    print("Square of the current number:", square)
    
    square_root = math.sqrt(i)
    print("Square root of the current number:", round(square_root, 2))
    
    total += i

average = total / n

print("The sum of numbers from 1 to", n, "is", total)
print("The average of the numbers from 1 to", n, "is", round(average, 2))