s=input()
x='bob'
c=0
for i in range(0,len(s)-2,1):
	if s[i]+s[i+1]+s[i+2]==x:
		c=c+1
print(c)


