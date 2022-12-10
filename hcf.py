def hcf(x,y):
	if x>y:
		smaller=y
	else:
		smaller=x
	for i in range(1,smaller+1):
		if(x%i==0 and y%i==0):
			hc=i
	return hc
x=int(input("Enter the Number"))
y=int(input("enter the number"))
print(hcf(x,y)) 
