# Triple quotes just after a function's signature (heading)
# creates a docstring. This docstring provides information about
# the function.


def add(item1, item2):
    '''
    Add two values together (a silly program)
    Parameters:
        item1: int/float/str
        item2: int/float/str

    Returns:
        returning value: int/float/str
    '''
    result = item1 + item2
    return result





def main():

    n1 = 4
    n2 = 5
    sum = add(n1,n2)
    print(sum)

    answer = add(9.7, 4.5)
    print(answer)

    print(add(9.7, 4.5))

    print(add("Hello", "!"))

    print(add.__doc__)

main()
