rrp = 10.49 

paid = float(input("How much did you pay? "))



if paid < rrp: 
    underpaid = paid - rrp
    percentage_overpaid = underpaid / rrp 
    print(f"you under paid by {percentage_overpaid}")
    

elif paid > rrp:
    overpaid = paid - rrp
    percentage_overpaid = overpaid / rrp 
    print(f"you overpaid by {percentage_overpaid}")
    
else: 
   print("you paid the rrp")
