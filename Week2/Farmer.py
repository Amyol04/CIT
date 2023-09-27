chickens = int(input("how many chickens do you own?"))
cows = int(input("how many cows do you own?"))
pigs = int(input("how many pigs do you own?"))
 
chickenLegs = chickens * 2 
cowsLegs = cows * 4 
pigsLegs = pigs*4

totalAmount = chickenLegs + cowsLegs + pigsLegs

print(f"The total amount of legs is {totalAmount}")

