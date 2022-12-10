n=input("Enter the String ").lower()
str=""
for i in n[::-1]:
	str+=i
if(n==str):
	print("Given String is A pallindrome ")
else:
	print("Given String is not a Pallindrome ")

'''
Enter the String "Krishna"
Given String is not a Pallindrome 

Enter the String "MadaM"
Given String is A pallindrome 

'''
