def onlyoneqn(listt):
    a = {}
    k = []
    v = []
    for i in listt:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    k = list(a.keys())
    v = list(a.values())
    return "Highest number of votes for question : Who should be the next Prime Minister? :"+" "+k[v.index(max(v))]
def main():
    numberofquestions = int(input())
    d = dict()
    qnslist = []
    for qns in range(0, numberofquestions):
        qntext = input()
        qnslist.append(qntext)
        newlist = []
        for options in range(0, 4):
            string = input()  
            newlist.append(string)
        d[qntext] = newlist
    nl = []
    dictt = dict()
    optionslist = []
    newl = []
    num = int(input())
    flatten = []
    for voters in range(num):
        p = input()
        nl.append(p)
        optionslist = []
        for k in range(numberofquestions):
            b = input().split(" ")
            optionslist.append(b[len(b) - 1])
        dictt[p] = optionslist
        newl.append(optionslist)
    for items in newl:
        for j in items:
            flatten.append(j)
    if len(flatten) == 3:
        print(onlyoneqn(flatten))
    else:
              pass
if __name__ == '__main__':
    main()