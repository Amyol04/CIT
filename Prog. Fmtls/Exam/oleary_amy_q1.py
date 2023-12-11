# Amy o leary
# R00246749

single = 100
double = 105 
family = 100
perChild = 50 

maxSpace = 4 
#discountCode = "Break15"

rooms = ("1: Single \n 2: double \n 3:family")

email = input("Email:")


roomRequired = int(input("What room would you like? 1-3"))
discountOffer = input("Discount Code:  (Press ENTER if none >> )")
discountCode = "Break15"

if roomRequired == 1: 
        room = ("single")
        cost = 100
        if discountOffer == discountCode: 
            cost = 0.85 * cost
            print("A discount code has been applied")
         
        
if roomRequired == 2: 
        room = ("double")
        cost = 105
        if discountOffer == discountCode: 
             cost = 0.85 * cost
             print("A discount code has been applied")

if roomRequired == 3:
    room = ("family")
    cost = 100 
    adultAmount = int(input("what are the number of adults"))
    childrenAmount= int(input("what are the number of children"))
    cost = cost * childrenAmount + cost
    
    
    

    if adultAmount + childrenAmount > maxSpace:
        print("sorry too much")
    
    if discountOffer == discountCode: 
         cost = 0.85 * cost
         print("A discount code has been applied")

        


print("-----------------------")
print(f"{email:} {room:}  {cost:}")
    
    
    
    	