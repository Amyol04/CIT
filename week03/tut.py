try: 
    x = int(input("number:"))
    y = int(input("number:"))
    print(x/y)

except ValueError:
    print("Sorry! That wsa not an interger number:( Lets try again!")
    7
except ZeroDivisionError: 
    print("cant devide by 0")

# try to do something, if it crashes then print the except.
