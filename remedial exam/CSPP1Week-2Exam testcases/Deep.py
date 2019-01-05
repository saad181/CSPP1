def list_sum(sumlist):
	count = 0
	for i in sumlist:
		for number in i:
			sum1 = sum1+int(number)
			return sum1
			print(sum1)


def list_count(count):
	tot = 0
	for i in count:
		if "[" in i:
			tot = tot+1
			return tot
			deduct = tot - 1

		# else:
			






def main():
	store = eval(input())
	print(list_sum(store))
	print(list_count(store))

if __name__ == '__main__':
	main()