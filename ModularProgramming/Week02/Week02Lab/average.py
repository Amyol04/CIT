def get_average():
    with open("cash_takings.txt", "r") as file:
        total = 0
        count = 0
        for line in file:
            number = int(line.strip())
            total += number
            count += 1

    if count > 0:
        average = total / count
        return average
    else:
        return "No numbers found in the file."

def main():
    result = get_average()
    print("Average:", result)

if __name__ == "__main__":
    main()
