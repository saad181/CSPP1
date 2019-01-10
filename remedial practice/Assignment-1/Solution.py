def loading(question):
	splitting = question.split(":")
	qns = splitting[0]
	choice = splitting[1]
	correct_ans = splitting[2]
	max_marks = splitting[3]
	penalty = splitting[4]
	qns_1 = qns.split(" ")
	print(qns+"("+str(qns_1[2])+")")
	choice_1 = choice.replace(",","	")
	print(choice_1)

# def score():
# 	print("|--------------|")
# 	print("| Score Report |")
# 	print("|--------------|")

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
		print()
	print("|--------------|")
	print("| Score Report |")
	print("|--------------|")
	start = input()
	quiz_token = start.split(" ")
	qu = quiz_token[1]
	print(qns)

		
main()	



