'''we ahve to find the perfect cube of a given input'''
# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm
# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube
# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
def main():
    '''finding the perfect cube'''
    # input is captured in s
    number = int(input())
    # watch out for the data type of value stored in s
    # your code starts here
    step = 0.1
    epsilon = 0.01
    guess = 0.0
    while guess <= number:
        if abs(guess**3-number) < epsilon:
            break
        else:
            guess += step
    if abs(guess**3-number) >= epsilon:
        print(str(number) + " is not a perfect cube")
    else:
        print(str(number) + " is a perfect cube")
if __name__ == "__main__":
    main()
