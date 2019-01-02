def getImage(image):
    string = image.split("<img")
    string= string[1:]
    # print(string)
    # start =" "
    l = []


    count = 0
    tag = "src=\""
    end = "\""
    for i in string:
        l.append(i)
        for items in l:
            if tag in items: 
                possible = items.index(tag)
                items = items[possible + len(tag):]
                ending = items.index(end)
                # print(ending)
                result=items[:ending]
                print(result)
        count=count+1
        print(result)
    print(count)
# def getBackground():
    








def main():
    file = open("webpage5.html", errors="ignore").read()
    inp = input()
    if inp == "image":
        getImage(file)
    # if inp == "background"  
    #     getBackground(file)
   
if __name__ == '__main__':
    main()