def quiz(l):
	token = l.split("|")
	stu_id  = int(token[0])
	ques = token[1]
	response = token[2]
	answer = token[3]
	points = int(token[4])
	count = 0
	d = dict()
	t = tuple(response, answer, points)
	st = d.keys(stu_id)
	options = d.values(t)
	if response == answer:
		count = count+ points
		total_score = (points/count)*100
	return count
	# else:
	# 	deduct = (points)









def main():
	inp = int(input())
	for i in range(0,inp):
		line = input()
		quiz(line)
main()
