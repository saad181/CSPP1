# Write a python program to find the square root of the given number
'''write the program using aprox method'''
# using approximation method
# testcase 1
# input: 25
# output: 4.999999999999998
# testcase 2
# input: 49
# output: 6.999999999999991
def main():
    ''' print the square root using aprox method'''
    num = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon = 0.01
    step = 0.1
    # your code starts here
    increment = 0.1
    while abs(step**2-num) >= epsilon:
        step = step+increment
    if not (abs(step**2-num) >= epsilon):
        print(str(step))
if __name__ == "__main__":
    main()