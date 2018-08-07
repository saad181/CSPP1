# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdIter(x, y):
	'''
	a, b: positive integers
	
	returns: a positive integer, the greatest common divisor of a & b.
	'''
	# Your code here
	
	
	if x<y:
		c = x
	else:
		c = y
	gcd = 0

	for i in range (1, c+1):
		if x%i == 0 and y%i == 0:
		  gcd = i
	return gcd	 





def main():
	data = input()
	data = data.split()
	print(gcdIter(int(data[0]),int(data[1]))) 

if __name__== "__main__":
	main()