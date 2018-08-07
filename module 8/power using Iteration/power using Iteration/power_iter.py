# Exercise: PowerIter
# Write a Python function, iterPower(base, exp), that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.
def iterPower(base1, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    base = base1
    if exp == 0:
        return 1
    else :
        for i in range(exp-1):
            base1 = base1*base
        return base1
         #n=0
    #while exp<n:
    #	res = base**exp
    #	exp = exp+1
    #	print(res)
def main():

    data = input()
    data = data.split()
    print(iterPower(float(data[0]),int(data[1]))) 

if __name__== "__main__":
    main()