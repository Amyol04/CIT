
def lines(): 
    print("=====")

def print_name_as_block(name): 
    for k in range(len (name)): 
        print(name * len (name))

def main(): 
    lines()
    print_name_as_block("Amy".upper())
    lines()

main()