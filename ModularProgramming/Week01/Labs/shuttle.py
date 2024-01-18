def draw_line():
    print("|    |") 

def draw_a_gappy_line():
    print("-----")

def draw_nose():
    print("/\\")
    print("/ \\")
    print("/  \\")



def draw_thrusters (): 
    draw_a_gappy_line()
    for k in range(3):
        draw_line()
    draw_a_gappy_line()
    print("draw plume")

def draw_shuttle():
    draw_nose()
    draw_thrusters() 

def main(): 
    draw_shuttle() 

main()