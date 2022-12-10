#Remove Characters at Even Indices
n=input("Enter the string")
new=""
for i in range(0,len(n)+1,2):
	new+=n[i]
print(new)

'''Output:
Enter the string"Krishna" 
Kiha'''

