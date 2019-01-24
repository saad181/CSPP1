def quiz(l):
	token = l.split("|")
	stu_id  = token[0]
	ques = token[1]
	response = token[2]
	answer = token[3]
	points = (token[4])
	total = dict()
	marksobtained = dict()
	try:
		if points == 'a':
			raise Exception("invalid points")
		else:
			if stu_id not in marksobtained:
				total[stu_id] = int(points)
				marksobtained[stu_id] = int(0)
			else:
				total[stu_id] = total[stu_id]+(points)
			if response == answer:
				marksobtained[stu_id] += points
			else:
				marksobtained[stu_id] -= points
				if marksobtained[stu_id] < 0:
					marksobtained[stu_id] += points
				else:
					marksobtained[stu_id]
		for keys in sorted(marksobtained):
			for each in sorted(total):
				if keys == each:
					score = (marksobtained[keys]/total[each] * 100)
					if score <=0:
						score = 0.0
						print(each + ": "+ str(score)+"%")
					else:
						print(each + ": "+ str(float(score))+ "%")
	except Exception as e:
		print(e)

	
def main():
	inp = int(input())
	for i in range(0,inp):
		line = input()
		quiz(line)
main()


