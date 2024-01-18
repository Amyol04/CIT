def show_tables(number):
    if number < 1 or number > 12:
        print("Error: Number must be between 1 and 12")
    else:
        for i in range(1, 13):
            product = i * number
            print(f"{number} * {i} = {product}")

def main():
    show_tables(10)  

if __name__ == "__main__":
    main()
