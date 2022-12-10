# Difference Between Two Lists
l1=[1,2,3,4,4,1,1,2,2]
l2=[1,2]
diff=[]
for i in l1:
	if i not in l2:
		diff.append(i)
print(diff)

#[3, 4, 4]
