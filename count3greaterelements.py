#Count Elements Greater than 3
l=[int(i) for i in input().split()]
c=0
for i in l:
	if(l.count(i)>3):
		c+=1
print(c)	
'''
1 2 3 4 5 6 12 2 3 12 3 1 2 12 1 2 3 4 5 2
9
'''
