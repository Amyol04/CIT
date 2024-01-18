



def draw_line():
    print("- -")

def draw_a_solid_line():
    print(f"+{3 * '-'}+")

def draw_box():
    for k in range(3):
        draw_line()
    draw_a_solid_line()


def main(): 
    draw_box()


main()