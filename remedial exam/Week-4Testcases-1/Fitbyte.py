def fit(l):
	i = 0
	token = l.split(",")
	logs = token[0]
	date = token[1]
	time = token[2]
	logs_split = logs.split(" ")
	activity = logs_split[0]
	type_act = logs_split[1]
	while(i<inp):
		print(activity+":"+date+":"+"- "+logs+":"+ type_act)





def main():
	inp = int(input())
	for i in range(0,inp):
		line = input()
		fit(line)
if __name__ == '__main__':
	main()
