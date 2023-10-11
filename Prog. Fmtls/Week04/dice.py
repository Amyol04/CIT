import random
n1 = random.randint(1, 6)
n2 = random.randint(1, 6)
print(n1, n2)

dice_sum = n1 + n2 

if n1 == n2 or dice_sum == 7 or dice_sum == 11:
    print("Lucky !! ")

else: 
    print("better luck next time")

print(f"dice 1 = {n1}")
print(f"dice 2 = {n2}")
print(f"the sum is {dice_sum}")
