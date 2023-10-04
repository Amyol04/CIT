score = int(input("how much did you score? "))
value_per_hole = int(input("What is the value per whole"))

diffrence = score - value_per_hole

if diffrence == -1:                                  
   print(f"Birdie!")
elif diffrence == 0:                        
   print(f"Par.")
elif diffrence == 1:
   print(f"Bogey")
elif diffrence > 1:                                 
   print(f"Double Bogey or worse.")
else:
   diffrence < -1:                                 
   print(f"Eagle or better.")
