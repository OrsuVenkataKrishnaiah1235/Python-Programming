n=int(input("Enter the number "))
temp=n
rev=0
while temp>0:
	digit=temp%10
	rev=rev*10+digit
	temp//=10
if(n==rev):
	print("Pallindrome")
else:
	print("Not a Pallindrome")
