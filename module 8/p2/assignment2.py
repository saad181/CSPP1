# Exercise: Assignment-2
'''to write a program that finds sum of digits'''
# Write a Python function, sumofdigits,
#that takes in one number and returns the sum of digits of given number.
# This function takes in one number and returns one number.
def sumofdigits(number):
    '''
    n is positive Integer
 returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if number == 0:
        return 0
    return number%10 + sumofdigits(number//10)
def main():
    '''this will print the sum of digits'''
    num = input()
    print(sumofdigits(int(num)))
if __name__ == "__main__":
    main()
    