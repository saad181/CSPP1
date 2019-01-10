def loading(question):
	splitting = question.split(":")
	qns = splitting[0]
	choice = splitting[1]
	correct_ans = splitting[2]
	max_marks = splitting[3]
	penalty = splitting[4]
	print(qns)








def main():
	inp = input()
	token = inp.split(" ")
	sp = int(token[1])
	print("|----------------|")
	print("| Load Questions |")
	print("|----------------|")
	print(str(sp)+" "+"are added to the quiz")
	print("|------------|")
	print("| Start Quiz |")
	print("|------------|")
	for i in range(0,sp):
		ques = input()
		loading(ques)


main()	



