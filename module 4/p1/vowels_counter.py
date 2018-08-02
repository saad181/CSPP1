'''Assume s is a string of lower case characters.'''
#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    '''count of vowels'''
    i = input()
    # the input string is in s
    # remove pass and start your code here
    vovels = ['a', 'e', 'i', 'o', 'u']
    vovelscount = 0

    for string in i:
        for i in vovels:
            if string == i:
                vovelscount += 1
    print('the vovel count is %s' %(vovelscount))
if __name__ == "__main__":
    main()
