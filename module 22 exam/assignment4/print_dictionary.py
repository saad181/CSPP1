'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    ''' this is used for the sorting of words and values'''
    for key, value in sorted(dictionary.items()):
        num = print(str(key)+" - "+str(value))
    return num
def main():
    ''' to check the dictionary'''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
#https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
 