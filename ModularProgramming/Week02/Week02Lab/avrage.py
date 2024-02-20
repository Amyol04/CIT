def get_average():
    try:
        # Create or open the file with cash takings
        with open("cash_takings.txt") as file:
            total = 0
            count = 0

            for line in file:
                line = line.rstrip()
                number = int(line)
                print(number)
                
                total += number
                count += 1

        # Calculate the average
        if count > 0:
            average = total / count
            return average
        else:
            print("No data found in the file.")
            return None

    except FileNotFoundError:
        print("Oops! File not found.")
        return None
    except ValueError:
        print("Oops! Some data isn't a number.")
        return None

def main():
    # Test and print the average value
    average_value = get_average()
    if average_value is not None:
        print(f"Average cash takings: {average_value}")

if __name__ == "__main__":
    main()