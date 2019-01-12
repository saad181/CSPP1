def quiz(l):
	token = l.split("|")
	stu_id  = int(token[0])
	ques = token[1]
	response = token[2]
	answer = token[3]
	points = token[4]
	print(stu_id)
	









def main():
	inp = int(input())
	for i in range(0,inp):
		line = input()
		quiz(line)
main()
