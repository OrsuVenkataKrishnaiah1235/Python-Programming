n=input("Enter the String ")
s=""
j=int(input("Enter the remove character position index "))
for i in range(len(n)):
	if j!=i:
		s+=n[i]
print(s)
'''
Enter the String "Krishna"
Enter the remove character position index 3
Krihna
'''
