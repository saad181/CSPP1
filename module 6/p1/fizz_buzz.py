'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    num = int(input())
    for num in range(1,num+1,1):
       if (num%3 == 0):
       	num += 1
        print("Fizz")

       elif (num%5 ==0):
        print("Buzz")
        num += 1
       elif (num%3 == 0 and i%5 == 0):
        print("Fizz")
        print("Buzz")
       else: 
        print (num)



if __name__ == "__main__":
    main()
