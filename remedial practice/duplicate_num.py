a = ["2", "5", "2", "9", "1", "1", "5", "3"]
result = dict((i, a.count(i)) for i in a)
#print(result.keys())
for i in result.keys():
	print(str(i) +" : "+ str(result[i]))



	