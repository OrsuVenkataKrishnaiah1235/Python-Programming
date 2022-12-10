#First and Last Three Characters of a String
n=input("Enter the input")
if (len(n)>6):
	print(str(n[:3])+str(n[(len(n)-3):]))
	
else:
	print(" ")
