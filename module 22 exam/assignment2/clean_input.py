'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    ''' clean the string by removing the special characters'''
    characters = ""
    clean = re.sub("\W+", '', string)
    characters = clean.replace(" ", "")
    return characters
def main():
    ''' This main fuction is used to call the clean string'''
    string = input()
    print(clean_string(string))
if __name__ == '__main__':
    main()
#https://stackoverflow.com/questions/5843518/
      #remove-all-special-characters-punctuation-and-spaces-from-string