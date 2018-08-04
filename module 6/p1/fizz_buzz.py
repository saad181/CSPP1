'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''program to find the replace multiple of 3 and 5 with fizz and buzz
    program to find fizz buzz
    Read number from the input, store it in variable num.
    '''
    num = int(input())
    for num in range(1, num+1, 1):
        if num%3 == 0 and num%5 == 0:
            print("Fizz")
            print("Buzz")
        elif num%3 == 0:
            print("Fizz")
            num += 1
        elif num%5 == 0:
            print("Buzz")
            num += 1
        else:
            print(num)
if __name__ == "__main__":
    main()
