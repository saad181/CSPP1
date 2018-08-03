# Write a p_numthon program to find the square root of the given number
'''writing newton rapson method to find square'''
# using approximation method
# testcase 1
# input: 25
# output: 4.999999999999998
# testcase 2
# input: 49
# output: 6.999999999999991
def main():
    '''using newton raphson method'''
    # epsilon and step are initialized
    # don't change these values
    # _numour code starts here
    _num = int(input())
    epsilon = 0.01
    guess = _num/2.0
    while  (guess**2-_num) >= epsilon:
        guess = guess - (((guess**2)-_num)/(2*guess))
    print(guess)
if __name__ == "__main__":
    main()
