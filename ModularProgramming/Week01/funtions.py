year = 2024 # global veriable 
def draw_line():
    width = 4 # local veri 
    print("*-*" * width)


def say_hello():
    print("how are you today")
    draw_line()
    print("goodbye")
    draw_line()

def say_goodbye():
    draw_line()
    print("good bye!")
    draw_line()


print("start")
say_hello()
print("How are you today!")