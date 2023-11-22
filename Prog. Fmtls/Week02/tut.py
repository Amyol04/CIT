#ProgFundem #2
#                                   ∞༺✦✮✦༻✧ Emoji and Arithmetic Operations ∞༺✦✮✦༻✧
print("\U0001F973", "\U0001F973", sep='******')  # Unicode for emojis
i = 7
f = 6.7
result1 = 7 // 5                      # Float division
result2 = 7 % 5                       # Division with remainder
result3 = 7 ** 5                      # 7 to the power of 5


#                                   ∞༺✦✮✦༻✧   Importing Math Module ∞༺✦✮✦༻✧ 
import math  # Adds math functions (cos, pi, etc...)
pi_value = math.pi  # Example using math.pi

#                                  ∞༺✦✮✦༻✧   User Input and Data Types ∞༺✦✮✦༻✧
class_name = input("What is the Class' name? ")
print(type(class_name), class_name)  # input function always returns a string

#                            ∞༺✦✮✦༻✧  String Concatenation and Type Conversion ∞༺✦✮✦༻✧
num1 = input("Number 1 >> ")
num2 = input("Number 2 >> ")
add_as_string = num1 + num2  # Adds as strings (e.g., "7" + "9.6" = "79.6")

#                                  ∞༺✦✮✦༻✧ Type Conversion to Integers ∞༺✦✮✦༻✧

num1 = int(input("Number 1 >> "))  # Convert string to int
num2 = int(input("Number 2 >> "))
add_as_int = num1 + num2  # Adds as integers

#                                    ∞༺✦✮✦༻✧ Type Conversion to Floats  ∞༺✦✮✦༻✧

num1 = float(input("Number 1 >> "))  # Convert string to float
num2 = float(input("Number 2 >> "))
add_as_float = num1 + num2  # Adds as floats

#                                   ♡━━━♡ Exercise 1: Coffee Cost Calculation ♡━━━♡
coffee_price = 2.20
quantity = int(input("How many coffees would you like?"))
total_cost = coffee_price * quantity
print(f"Total Cost for {quantity} cups of coffee is: €{total_cost:.2f}")

#                                  ♡━━━♡ Exercise 2: Product Cost Calculation with Discount ♡━━━♡
description = input("Description of Product")
cost = float(input("How Much is The Product"))
reduction = float(input("Discount?"))
total_cost_with_discount = cost - cost * (1 - reduction)
print(f"The Total cost for {description.lower()} is: €{total_cost_with_discount:.2f} with the student discount.")

#                            ♡━━━♡ Exercise 3: Circle Area and Circumference Calculation ♡━━━♡
import math
radius = float(input("What is the circle's radius?"))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"Area is {area:.4f} and circumference is {circumference:.4f}")

#                                ∞༺✦✮✦༻✧   F-Strings for Formatting ∞༺✦✮✦༻✧
name1, name2, name3 = "Conan", "Amy", "James"
age1, age2, age3 = 5, 19, 19
name_heading, age_heading = "Name", "Age"
print(f"{name_heading:^12}{age_heading:^10}")  # Center align headings
print('-' * 22)
print(f"{name1:>12}{age1:10}")  # Right align names, left align ages
print(f"{name2:>12}{age2:10}")
print(f"{name3:>12}{age3:10}")

#                             ∞༺✦✮✦༻✧ Formatting Percentages and Commas ∞༺✦✮✦༻✧
discount = 0.2
print(f"The Discount is {discount:%}")  # Displays percentage with 0 decimal places
wages = 12345.98
print(f"The Wages are €{wages:,.}")  # Adds commas for thousands in numbers

#                              ∞༺✦✮✦༻✧  Book Titles and Total Price Calculation ∞༺✦✮✦༻✧
title1 = input("Title of the book: ")
cost1 = float(input(f"Price of '{title1}': "))
title2 = input("Title of the book: ")
cost2 = float(input(f"Price of '{title2}': "))
total_price = cost1 + cost2

#                             Displaying Book Details and Total Price
print(f"{title1:20}€{cost1:.2f}")
print(f"{title2:20}€{cost2:.2f}")
print("=" * 30)
print(f"Total Price: {'€':>15}{total_price:.2f}")  # Right aligns and formats the total price
