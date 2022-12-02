n=int(input("enter the Number"))
temp=n
Sum=0
while(temp>0):
	digit=temp%10
	Sum+=digit**3
	temp//=10
if(n==Sum):
	print("Armstrong Number")
else:
	print("Not a arm Strong Number")
