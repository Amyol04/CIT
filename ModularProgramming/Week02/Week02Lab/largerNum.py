def findLargerNum(num1, num2): 
    if num1 > num2: 
        return num1
    
    if num2 > num1: 
        return num2
    else: 
        return num1
    
def main(): 
    num1 = 6 
    num2 = 7 
    result = findLargerNum(num1,num2)

    print(f"larger num is {result}")

main()

    