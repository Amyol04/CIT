IRELAND_TIPPING = 0.10
USA_MIN = 0.15 
USA_MID = 0.18 
USA_NORM = 0.20 


cost = float(input("how much is the food bill"))

ireland_tip = IRELAND_TIPPING * cost 
usa_least = USA_MIN * cost 
usa_ok = USA_MID * cost 
usa_norm = USA_NORM * cost 

print(f"{'tip':10}{'value':>10}")
print("-----------------------")
print(f"{IRELAND_TIPPING}<10.0%{ireland_tip}<10.2f")
print(f"{USA_MIN}<10.0%{usa_least}<10.2f")
print(f"{USA_MID}<10.0%{usa_ok}<10.2f")
print(f"{USA_NORM}<10.0%{usa_norm}<10.2f")
