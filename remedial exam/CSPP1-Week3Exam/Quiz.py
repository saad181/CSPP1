def quiz(l):
	token = l.split("|")
	stu_id  = int(token[0])
	ques = token[1]
	response = token[2]
	answer = token[3]
	points = int(token[4])
	count = 0
	d = dict()
	li = list()
	li.append(response,answer,points)
	k = d.keys()
	v = d.values(li)
	for k,v in sorted(d):
		if response == answer:
			count = count+ points
			total_score = (points/count)*100
	print((stu_id)+":"+" "+int(total_score))
	# else:
	# 	deduct = (points)



def main():
	inp = int(input())
	for i in range(0,inp):
		line = input()
		quiz(line)
main()
