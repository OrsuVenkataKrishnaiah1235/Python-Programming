#Remove Matching Element
l=[int(i) for i in input().split()]
r=eval(input("Enter the Remove Element "))
if not l:
	print("Empty list")
elif l.count(r)==0:
	print("Removed element not in the list ")
else:
	l.remove(r)
print(l)
