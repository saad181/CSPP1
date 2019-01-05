def list_sum(sumlist):
	count = 0
	for i in sumlist:
		sum =0
		for y in i:
			sum = sum + y
			print(sum)







def main():
	store = input()
	list_sum(store)
if __name__ == '__main__':
	main()