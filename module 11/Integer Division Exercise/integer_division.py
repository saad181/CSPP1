#Exercise: Integer Division Exercise
'''division of integer'''
#Modify the code for integer_division so that this error does not occur.

def integer_division(x_x, a_a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x_x >= a_a:
        count += 1
        x_x = x_x - a_a
    return count
def main():
    '''main function'''
    data = input()
    data = data.split()
    print(integer_division(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()