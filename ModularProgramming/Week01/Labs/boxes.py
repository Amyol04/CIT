hight = int(input("what height box ?"))


def draw_a_gappy_line(): 
    print("-----")


def hight_box(): 
    for i in range(hight): 
        print("|    |")

def draw_box(): 
    draw_a_gappy_line()
    hight_box()
    draw_a_gappy_line()

def main():
    draw_box()

main() 
