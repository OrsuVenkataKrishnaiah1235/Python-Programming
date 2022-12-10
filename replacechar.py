#Replace a Character in a String
n=input("Enter the String ")
j=input("Enter the Actual Character to replace ")
i=input("Enter the Character to replace ")
new_str=""
for char in n:
	if char==j:
		new_str+=i
	else:
		new_str+=char
print(new_str)

'''
Enter the String "Krishna"
Enter the Actual Character to replace "a"
Enter the Character to replace "m"
Krishnm
'''
#or simply
print(n.replace(j,i))

