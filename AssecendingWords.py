#Sort Words in Alphabetical Order
n=input("Enter the String ")
new_str=""
k=n.split()
for i in k:
	l=i.lower()
	m="".join(sorted(l))
	new_str+=m
new_str.strip()
print(new_str)
