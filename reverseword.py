n=input("Enter the input")
'''
n[::-1]
Enter the input"KRISHNAiah"
haiANHSIRK
'''
n=n.split()
new_str=""
for word in n:
	words=word[::-1]
	swap_case=words.swapcase()#used for loewr to high and higher to lower swapping
	new_str+=swap_case
new_str.rstrip()
print(new_str)
'''
Enter the input"Hello Krishna"
OLLEhANHSIRk
'''
