def list_sum(sumlist):
	count = 0
	for i in sumlist:
		for number in i:
			print(number)







def main():
	store = list(input())
	list_sum(store)
if __name__ == '__main__':
	main()