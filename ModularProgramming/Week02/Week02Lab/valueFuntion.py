## What will you call the function?
## How will you call the function?
## How will you define the function?
def calc_Miles(miles): 
    km = miles * 0.6214
    return km

def main(): 
    miles = 32
    sum = calc_Miles(miles)
    print(sum)


main()