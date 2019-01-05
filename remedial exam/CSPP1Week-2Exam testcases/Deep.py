def list_sum(sumlist):
	count = 0
	for i in sumlist:
		if isinstance(i,list):
			count = count+list_sum(i)
		else:
			count = count+i
	return count

		

			


def list_count(count):
	tot = 0
	for i in count:
		if "[" in i:
			tot = tot+1
	return tot
	deduct = tot - 1
	print(deduct)

def depth(d):
    maxi = 0
  
    # traversal in the lists 
    for x in list1: 
        sum = 0 
        # traversal in list of lists 
        for y in x: 
            sum+= y      
        maxi = max(sum, maxi)  
          
    return maxi 


def main():
	sumlist = eval(input())
	list_sum(sumlist)
	list_count(store)
	depth(store)

if __name__ == '__main__':
	main()