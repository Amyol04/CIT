BLUE = "\033[1;34m"
RED = "\033[91m"
RESET = "\033[0m"

def sing(name):
    print(f"{BLUE}'name' is {name}{RESET}")
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print("Happy Birthday dear", name)
    print("Happy Birthday to you!")
    name = "Mickey Mouse"
    print(f"{BLUE}'name' is {name}{RESET}")

def main():
    name = "Fred"
    print(f"{RED}'name' is {name}{RESET}")
    sing(name)
    sing(199)
    # Note: name has not become "Mickey Mouse"!
    print(f"{RED}'name' is {name}{RESET}")
    main()