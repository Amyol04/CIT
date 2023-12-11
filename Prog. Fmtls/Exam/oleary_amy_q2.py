# Amy o leary
# R00246749
def log_test_results(email,room,cost):
   with open("test_log.txt", "a") as file:
       file.write(f"Email: {email:}, Room: {room:}  Cost:{cost:}, Cost of BREAK15{discountTogether} \n Cost of booking{average}\n")
       
       
def gmail(email,room,cost):
   with open("gmail.txt", "a") as file:
       file.write(f"Email: {email:}, Room: {room:}  Cost:{cost:}\n")

while True: 

    single = 100
    double = 105 
    family = 100
    perChild = 50 
    average = 0
    bookingAmount = 0 
    discountTogether = 0 
    discountTotal = 0 


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
            bookingAmount += 1
            if discountOffer == discountCode: 
                cost = 0.85 * cost
                print("A discount code has been applied")
                discountTotal += 1
    
            
            
    if roomRequired == 2: 
            room = ("double")
            cost = 105
            bookingAmount += 1
            if discountOffer == discountCode: 
                cost = 0.85 * cost
                print("A discount code has been applied")
                discountTotal += 1
                

    if roomRequired == 3:
        bookingAmount += 1
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
            discountTotal += 1

            
    log_test_results(email, room , cost,)

    if email == "gmail.com":
        gmail(email,cost,)


        

    average = bookingAmount / cost
    discountTogether = discountTotal / cost

    print("-----------------------")
    print(f"{email:} {room:}  {cost:}")