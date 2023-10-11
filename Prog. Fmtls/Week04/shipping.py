weight = float(input("How much does it weigh (in kg): "))
distance = float(input("What is the distance (in km): "))

if weight <= 2: 
    shipping = 0.50 * distance

elif weight >= 10: 
    shipping = 2.50 * distance

elif 2 < weight <= 10:  
    shipping = 1.00 * distance

if distance > 500:
    discount = 0.10 * shipping
    shipping -= discount
    print("10% discount has been applied ")

print(f"Total shipping cost: €{shipping:.2f}")





