def main():
    inp = int(input())
    l = []
    for i in range(inp):
        tokens = input().split(" ")
        if tokens[0] == "reserve":
            getReserve(tokens[1])
        elif tokens[0] == "reserveN":
            getN(tokens[1], tokens[2])
        elif tokens[0] == "build":
            getBuild()
        elif tokens[0] == "cancel":
            cancel()
if  __name__ == '__main__':
        main()  

def getReserve(person):
    roomnum = 0
    dictionary = {}
    lis = []
    total_rooms = 5
    roomnum = roomnum+1
    if roomnum>total_rooms:
        print("All Rooms are reserved")
        return
    if roomnum not in dictionary.values():
        dictionary[person] = roomnum
        lis.append(roomnum)
        print(person+" "+ roomnum)
    else:
        reserve(person)    




    

def getN(person, roomnum):
    total_rooms = 5
    for room in sorted(lis):
        if int(roomnum) == int(room):
            print("All Rooms are reserved")
            return
    for room in dictionary.values():
        if int(roomnum) == int(room):
            print("Room is already reserved")
            return
        if int(roomnum) >= total_rooms:
            print("All Rooms are reserved") 
            return               






