def getImage(image):
	string = image.split("<img")
	count = 0
	start = "./webpage5\""
	end = ".jpg\""
	for eachthing in string:

		if start in eachthing:
			try:
				possible = eachthing.index(start)
				count = count+1
				eachthing = eachthing[length(start): end]
				ending = eachthing.index(end)
				# count = count+1

			except:
				pass
			else:
				print(eachthing[:end])









def main():
    file = open("webpage5.html", errors="ignore").read()
    getImage(file)
    # print(file)
   
if __name__ == '__main__':
    main()