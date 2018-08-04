'''
''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    string1 = input()
    string2 = ""
    for char in string1:
        if char in '!@#$%^&*':
            string2 = string2 + " "
        #print(" ")
        else:
            string2 = string2 + char
    print(string2) 
        #string3 = string1 + string2
if __name__ == "__main__":
    main()
