# Flatten a List that Contains Lists ()
l=[[1,2,3],[4,5,6],[7,8,9]]
flatten=[]
for elem in l:
	if isinstance(elem,list):
		for newelem in elem:
			flatten.append(newelem)
	else:
		flatten.append(elem)
print(flatten)

'''
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
