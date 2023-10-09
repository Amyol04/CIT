name1 = (input("what is your name?"))
name2 = (input("what is your name?"))
name3 = (input("what is your name?"))

age1 = int(input("what is your age"))
age2 = int(input("what is your age"))
age3 = int(input("what is your age"))

grade1 = float(input("what grade did you get?"))
grade2 = float(input("what grade did you get?"))
grade3 = float(input("what grade did you get?"))


print(f"{'Name':10}{'Age':>10}{'Grade':>10}")
print("-----------------------")
print(f"{name1}<10.0%{age1}<10.0%{grade1}<10.0%")
print(f"{name2}<10.0%{age2}<10.0%{grade2}<10.0%")
print(f"{name3}<10.0%{age3}<10.0%{grade3}<10.0%")
