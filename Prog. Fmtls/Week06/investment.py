lump_sum = float(input("Lump sum >>> "))
saving = float(input("Target >>> "))
# asks for lump sum and savings target 

annual_interest_rate = 0.0075
year = 0
current_balance = saving

print(f'Year{year}: €{current_balance:.2f}')

while current_balance < saving:
    year += 1
    current_balance += current_balance * annual_interest_rate
    print(f'Year{year}: €{current_balance:.2f}')

print(f"It will take {year} years to reach the savings target of €{saving:.2f}.")
