# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    i=0
    if char == aStr[i]:
      return True
    for i in range(len(aStr)):
        if char!= aStr[i]:
            return isIn(char, aStr[i+1:])
    return False 
    if i == len(aStr):
        return False    

   

def main():
    data = input()
    data = data.split()
    print(isIn((data[0]), data[1]))


if __name__ == "__main__":
    main()