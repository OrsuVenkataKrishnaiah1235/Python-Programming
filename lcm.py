def lcm(x,y):
	if x>y:
		greater=x
	else:
		greater=y
	while(True):
		if(greater%x==0 and greater%y==0):
			lc=greater
			break
		greater+=1
	return lc
x=int(input("Enter the Number"))
y=int(input("Enter the number"))
l=lcm(x,y)
print(l)
