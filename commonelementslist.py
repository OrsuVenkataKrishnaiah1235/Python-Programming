#Common Elements in Two Lists
l=[1,2,3,3,42,1,2]
k=[1,3,2]
m=[]
for i in l:
	if i in k:
		m.append(i)
print(m)

#[1, 2, 3, 3, 1, 2]
