hair = int(input("How big do you want the hair?"))
eyes = input("Is he surprised?")
nose = int(input("What nose would you like? 1. X 2. * "))

def draw_hair():
    for i in range(hair):
        print("####" * hair)

def draw_eyes():
    if eyes.lower() == "yes":
        print("- -")
        print("o o")
    elif eyes.lower() == "no":
        print("^ ^")
        print("O O")

def draw_nose():
    if nose == 1:
        print("x")
    elif nose == 2:
        print("*")
    else:
        print("w")

def draw_mouth():
    print("===")

def draw_face(): 
    draw_hair()
    draw_eyes()
    draw_nose()
    draw_mouth()

def main(): 
    draw_face()

main()