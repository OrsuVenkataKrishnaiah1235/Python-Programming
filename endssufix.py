#Check if a String Ends with a Suffix
n=input("Enter the input")
sufix=input("Enter the input of Sufix")
if(n[len(sufix)-1:]==sufix):
	print("True")
else:
	print("False")
print(n.endswith(sufix))


