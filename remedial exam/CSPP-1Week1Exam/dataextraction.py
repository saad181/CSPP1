def getImage(image):
	string = image.split("src")
	count = 0
	start = "./webpage5"
	end = ".png"
	for eachthing in string:
		if "./webpage5" in eachthing:
			try:
				pos = eachthing.index(start)
				eachthing = eachthing[pos+length(start): end]
				ending = eachthing.index(end)
				count = count+1
			except:
				pass
			else:
				print(eachthing[:ending])		








def main():
    file = open("webpage5.html", errors="ignore").read()
    getImage(file)
    
   
if __name__ == '__main__':
    main()