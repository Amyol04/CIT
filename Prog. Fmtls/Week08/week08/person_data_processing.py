table = f"{'Name':20}{'Age':10}\n"

while True:
    try:
        number_of_people = int(input("Enter the number of people: "))
        if number_of_people > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

oldest_age = float('-inf')
youngest_age = float('inf')
oldest_names = ""
youngest_names = ""
total_age = 0

for _ in range(number_of_people):
    name = input("Enter the name: ")
    
    while True:
        try:
            age = int(input("Enter the age: "))
            if age >= 0:
                break
            else:
                print("Please enter a non-negative integer for age.")
        except ValueError:
            print("Invalid input. Please enter a non-negative integer for age.")

    table += f"{name:20}{age:10}\n"

    total_age += age
    if age > oldest_age:
        oldest_age = age
        oldest_names = name
    elif age == oldest_age:
        oldest_names += f", {name}"

    if age < youngest_age:
        youngest_age = age
        youngest_names = name
    elif age == youngest_age:
        youngest_names += f", {name}"

average_age = total_age / number_of_people
print("\nAverage Age:", round(average_age, 2))

print("\nData:")
print(table)
print(f"\nOldest person(s): {oldest_names}, Age: {oldest_age}")
print(f"Youngest person(s): {youngest_names}, Age: {youngest_age}")
