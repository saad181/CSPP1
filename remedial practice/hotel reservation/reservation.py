from operator import itemgetter
global d
d = {}
global countofrooms
countofrooms = 0
global listt
listt = []
global total
total = 6

def getReserve(person):
    global countofrooms
    global d
    global total
    countofrooms += 1
    if countofrooms >= total:
        print("All Rooms are reserved")
        return
    if countofrooms not in d.values():
        d[person] = countofrooms
        listt.append(countofrooms)
        print(person + " " + str(countofrooms))
    else:
        reserve(person)

def getN(person, rn):
    global total
    for everyroom in sorted(listt):
        if int(rn) == int(everyroom):
            print("All Rooms are reserved")
            return
    for everyroom in d.values():
        if int(rn) == int(everyroom):
            print("Room is already reserved")
            return

        if int(rn) >= total:
            print("All Rooms are reserved")
            return
    d[person] = int(rn)
    print(person + " " + str(rn))


def getDisplay():
    for key, value in sorted(d.items(), key = itemgetter(1)):
        print(key, value)

def getBuild(extra):
    global total
    print("Added " + str(extra) + " more rooms")
    total += extra

def main():
    n = int(input())
    tokens = []
    for i in range(n):
        tokens = input().split(" ")
        if tokens[0] == "reserve":
            getReserve(tokens[1])
        elif tokens[0] == "reserveN":
            getN(tokens[1], tokens[2])
        elif tokens[0] == "print":
            getDisplay()
        elif tokens[0] == "build":
            getBuild(int(tokens[1]))
if __name__ == '__main__':
    main()