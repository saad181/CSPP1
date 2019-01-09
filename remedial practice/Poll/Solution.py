global b
b = []
global q1ans
q1ans = []
global q2ans
q2ans = []
global q3ans
q3ans = []
def convert(l):
    d = {}
    for j in l:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
    k = list(d.keys())
    v = list(d.values())
    return k[v.index(max(v))]
def print1():
    return "Highest number of votes for question : Who should be the next Prime Minister? : "
def print2():
    return "Highest number of votes for question : Who will be the next cm for Telangana? : "
def print3():
    return "Highest number of votes for question : Who will be the next cm for AP? : " 
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
    elif len(flatten) == 9:
        for i in newl:
            q1ans.append(i[0])
            q2ans.append(i[1])
            q3ans.append(i[2])
        convert(q1ans)
        convert(q2ans)
        convert(q2ans)
        print(print1()+convert(q1ans))
        print(print2()+convert(q2ans))
        print(print3()+convert(q3ans))
    else:
        for i in newl:
            q1ans.append(i[0])
            q2ans.append(i[1])
            q3ans.append(i[2])
        convert(q1ans)
        convert(q2ans)
        convert(q2ans)
        print(print1()+convert(q1ans))
        print(print2()+convert(q2ans))
        print(print3()+convert(q3ans))
main()
