#Second Largest Value in a List
l=[87,23,1,23,3,21,23,87,4,2]
m=sorted(l)
l=list(set(m))
k=[]
for i in range(0,len(l)-1):
	if(l[i]>l[i+1]):
		temp=l[i]
		l[i]=l[i+1]
		l[i+1]=temp
print(l)
print(l[-2])

'''
[1, 2, 3, 4, 21, 23, 87]
23
'''
