#Remove Spaces from a string

n=input("Enter the String ")
new_str=""
m=" "
for i in n:
	if i==m:
		continue
	else:
		new_str+=i
print(new_str)


'''
Enter the String "krishna Krishna"
krishnaKrishna

'''
