#Second Smallest Value in a List
l=[1,2,2,2,12,2,3,4,44,4,3,312,33,33]
l=sorted(l)
l=list(set(l))
for i in range(0,len(l)-1):
	if(l[i]>l[i+1]):
		l[i],l[i+1]=l[i+1],l[i]
print(l)
print(l[1])

'''
[1, 2, 3, 4, 12, 33, 44, 312]
2
'''
