def findLargerStr(str1, str2): 
    if len(str1) > len(str2): 
        return str1
    
    if len(str2) > len(str1): 
        return str1
    else: 
        return str1

def main(): 
    str1 = "pat"
    str2 = "joe"

    result = findLargerStr(str1, str2)
    print("the larger string is", result)

main()