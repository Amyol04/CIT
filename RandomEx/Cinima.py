ticket_price = 8.00
snack_box_price = 4.00

movie = input("what movoe would you like to watch? ")

ticket = float(input("how many tickets would you like to buy? "))
snack_box = float(input("how many snackbox's would you like to buy? "))

money = float(input("how much money are you tendering ? "))

ticket_total = ticket  * ticket_price 
snack_toital = snack_box * snack_box_price
trip_total = ticket_total + snack_toital
change = money - trip_total

if money < trip_total: 
    print("sorry not enough")
    
else:
    print(f"The Movie Name Is {movie}, The Trip will cost {trip_total} and your change is {change}")
