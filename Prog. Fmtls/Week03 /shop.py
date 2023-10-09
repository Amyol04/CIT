milk = float(input("How much is the milk ? "))
bread = float(input("How much is some bread"))

Milk_amount = int(input("How many liters of milk do you require? "))
Bread_amount = int(input("How much bread do you need"))

milk_sum = milk + Milk_amount
bread_sum = bread + Bread_amount

total = milk_sum + bread_sum

final_cost = total-total / 10


print(f"{'Item':10}{'amount':10}{'price':10.2f}{'amount after discount':10.2f}")
print("-"*20)
print(f"{'milk':10}{Milk_amount:10}{milk:10.2f}{milk_sum:10.2f}")
print(f"{'bread':10}{Bread_amount:10}{bread:10.2f}{bread_sum:10.2f}")
