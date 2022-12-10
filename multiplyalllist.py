# Multiply all Elements in a List
n=[int(i) for i in input().split()]
factor=2
for i in range(0,len(n)):
	n[i]*=factor
print(n)

'''
2 3 4 5
[4, 6, 8, 10]
'''
