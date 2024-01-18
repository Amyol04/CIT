def draw_a_solid_line():
    print(f"+{10 * '-'}+")


def draw_a_gappy_line():
    print(f"+{10 * ' '}+")


def draw_box(hight_of_box = 3):
    draw_a_solid_line()
    for k in range(3):
        draw_a_gappy_line()
    draw_a_solid_line()

def main():
    for i in range(1,4):
        draw_box()


print("xxxx\\xxxx")
main()
