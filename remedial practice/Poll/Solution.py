def equation():
	options = []
	partcipant = []
	d = {}

	for i in inp:
		
		for i in options:
			options.append(i)
def main():
    ques = int(input())
    d = dict()
    questionlist= []
    for qns in range(0, ques):
        questiontext = input()
        questionlist.append(questiontext)
        new = []
        for options in range(0,4):
            choice = input()
            new.append(choice)
        d[questiontext] = new
    new1 = []
    dictionary = dict()
    optionslist = []
    # print("s..........................")
    n1 = []
    num = int(input())
    emptylist = []
    for voters in range(0, num):
        p = int(input())
        new1.append(p)
        optionslist = []
        for k in range(ques):
            b = input.split(" ")
            optionslist.append(b[len(b) - 1])
        dictionary[p] = optionslist
        n1.append(optionslist)
    for items in n1:
        for j in items:
            emptylist.append(j)
    if len(emptylist) == 3:
        print(equation(emptylist))
    else:
        pass
if __name__ == '__main__':
    main()



		



