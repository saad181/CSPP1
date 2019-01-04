from operator import itemgetter
global dictionary
dictionary = {}
global roomnum
roomnum = 0
global listt
listt = []
global total
total = 6

def reserve(person):
    global roomnum
    global dictionary
    global total
    roomnum += 1
    if roomnum >= total:
        print("All Rooms are reserved")
        return
    if roomnum not in dictionary.values():
        dictionary[person] = roomnum
        listt.append(roomnum)
        print(person + " " + str(roomnum))
    else:
        reserve(person)

def reserveN(person, roomnum):
    global total
    for everyroom in sorted(listt):
        if int(roomnum) == int(everyroom):
            print("All Rooms are reserved")
            return
    for everyroom in dictionary.values():
        if int(roomnum) == int(everyroom):
            print("Room is already reserved")
            return

        if int(roomnum) >= total:
            print("All Rooms are reserved")
            return
    dictionary[person] = int(roomnum)
    print(person + " " + str(roomnum))


def display():
    for key, value in sorted(dictionary.items(), key = itemgetter(1)):
        print(key, value)

def build(extra):
    global total
    print("Added " + str(extra) + " more rooms")
    total += extra

def main():
    inp = int(input())
    tokens = []
    for i in range(inp):
        tokens = input().split(" ")
        if tokens[0] == "reserve":
            reserve(tokens[1])
        elif tokens[0] == "reserveN":
            reserveN(tokens[1], tokens[2])
        elif tokens[0] == "print":
            display()
        elif tokens[0] == "build":
            build(int(tokens[1]))
if __name__ == '__main__':
    main()