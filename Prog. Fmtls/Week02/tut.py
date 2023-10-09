#ProgFundem #2
print("\U0001F973", "\U0001F973", sep='******') #\u0001F73 - Unicode for emojis
i = 7
f = 6.7
7 // 5 # float division
7 %  5# division with a remainder
7 ** 5 #7 to the power of 5 # can be decimal (learned in lab)
import math #lab recap #adds math functions (cos, pi, ect...) (inf-infinate nan-not a number)
math.pi #example
# Recap ^^^


class_name = input("What is the Class' name? ")
print(type(class_name), class_name) #(input function always a string)


num1 = input("Number 1 >> ")
num2 = input("Number 2 >> ")
add = num1 + num2
print(type(add), add) #(adds as strings ~~ 7 + 9.6 = 79.6) (cant do minus between 2 strings)


num1 = int(input("Number 1 >> ")) #add int(interager) to convert string to int
num2 = int(input("Number 2 >> "))
add = num1 + num2
print(type(add), add)


num1 = float(input("Number 1 >> ")) #add float to convert string to float
num2 = float(input("Number 2 >> "))
add = num1 + num2
print(type(add), add)




# functions- types ^^^


#int - no decimal
#float - decimal number


#exersise  
#1
coffee_price = 2.20
quantity = int(input("How many coffees would you like?"))
total_cost = coffee_pice * quantity
print(f"Total Cost for {quantity} cups of coffee is: "f"€{total_cost:.2f}") # :.2f  colon: instructions .2f- 2 digits after the decimal


#2
description = (input("Description of Product"))
cost = float(input("How Much is The Product"))
reduction = float(input("Discount?"))
total_cost = cost - price*(1 - reduction)
print(f"The Total cost for {description.lower} is: "f"€{total_cost:.2f}"f"with the student discount.")


#3
import math
radius = float(input("What is the circles radius?"))


area = math.pi * radius ** 2
circ = 2 * math.pi * radius
print(f"Area is {area:.4f} and circumerence is {circ:.4f}")




name1 = "conan"
name2 = "amy"
name3 = "james"


age1 = 5
age2 = 19
age3 = 19


name_heading = "name"
age_heading = "age"


print(f"{name_heading:^12}{age_heading:^10}") #< -left > - right ^- middle
# print(f"{'Name':^12}{'Age':^10}") #alternative way with minimal variables
print('-') *22
print(f"{name1:>12}{age1:10}") # :10 - colum of 10/12
print(f"{name2:>12}{age2:10}")#  :> override defualt behaviour - letters left & numbers right
print(f"{name3:>12}{age3:10}")


#f strings - illustrating ^^^^




discount = 0.2
print(f"The Discount is {discount:%}.") # :.0%- Adds pecent sign afer colon ~ .0 - removes 6 digits after decimal
wages = 12345.98
print(f"The Wages are €{wages:,}.") #Adds comma every thousand/ where they need to be
#Commas & percentages ^^^


#question
title1 = input("title of the book : ")
cost1 = float(input(f"Price of '{title1}': "))


title2 = input("title of the book : ")
cost2 = float(input(f"Price of '{title2}': "))
total = cost1 + cost2


print(f"{title1:20}€{cost1:.2f}")
print(f"{title2:20}€{cost2:.2f}")
print("="*30)
print(f"'{Total Price:':20}€{total:.2f}")
