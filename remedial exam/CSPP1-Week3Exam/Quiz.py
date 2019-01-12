def quiz(l):
	token = l.split("|")
	stu_id  = int(token[0])
	ques = token[1]
	response = token[2]
	answer = token[3]
	points = int(token[4])
	count = 0
	if response == answer:
		count = count+ points
	









def main():
	inp = int(input())
	for i in range(0,inp):
		line = input()
		quiz(line)
main()
