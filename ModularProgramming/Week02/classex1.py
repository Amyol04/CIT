def calc_age(name, age):
    print(name, age)
    n1 = age % 10
    years_remaining = 10 -n1
    print(f"{name} {years_remaining} years to the next big birthday")

def main(): 

    print("xx")
    calc_age("anne", 22)


main()