#Check if a String Starts with a Prefix
n=input("Enter String")
prefix=input("Enter the prefix")
if(n[:len(prefix)]==prefix):
	print("True")
else:
	print("False")
'''
Enter String"Krishna"
Enter the prefix"Kri"
True
'''
#or simply using Method
print(n.startswith(prefix))

