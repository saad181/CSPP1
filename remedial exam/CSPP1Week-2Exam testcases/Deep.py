def list_sum(sumlist):
	count = 0
	for i in sumlist:
		for number in i:
			count = count+str(number)
			return count
			# print(count)








def main():
	store = eval(input())
	print(list_sum(store))

if __name__ == '__main__':
	main()