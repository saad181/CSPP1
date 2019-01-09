def lickme(l):
	qns = l[0]
	choices = l[1]
	correctchoice = l[2]
	maxmarks = l[3]
	penalty = l[4]
	ql = qns.split(" ")
	srno = q1[2]
	print(qns+"("+srno+")")
	temp = choices.split(",")
	for i in temp:
		print(i, end="\t")
		if i == 'choice 4':
			print(i, end="")
def fuckme(strings):
	listt = strings.split(":")
	lickme(listt)
def main():
	inp = input()
	split = inp.split(" ")
	sp = int(split[1])
	print("|----------------|")
	print("| Load Questions |")
	print("|----------------|")
	print(str(sp)+" "+"are added to the quiz")
	print("|------------|")
	print("| Start Quiz |")
	print("|------------|")
	for i in range(0,sp):
		st = input()
		fuckme(st)
main()
