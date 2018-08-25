'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def main():
    ''' To read the multiple lines of text'''
    read = ""
    length = int(input())
    for i in range(length):
        del i
        read = input()
        print(read)
if __name__ == '__main__':
    main()
