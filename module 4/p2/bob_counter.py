'''Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
 For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2'''
def main():
    '''prints the occurance of bob'''
    string = input()
    string1 = 'bob'
    counter = 0
    for i in range(0, len(string)-2, 1):
        if string[i]+string[i+1]+string[i+2] == string1:
            counter += 1
    print(counter)
if __name__ == "__main__":
    main()
