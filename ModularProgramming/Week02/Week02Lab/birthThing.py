def getAge(): 
  yearBirth = int(input("enter your year of birth")) 
  age = 2023 - yearBirth 
  return age


def cost(age): 
  if age < 10: 
    return 5.00
  if age < 21: 
    return 10.00
  else: 
    return 15.00
  
def main():
   age = getAge()
   print(age)
   result = cost(age)
   print(f"youre being charged {result}")

main()


