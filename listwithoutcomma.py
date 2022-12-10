#Print Elements on the Same Line Without Commas
l= 2,3,4,5,5,3,2,4,4,2 #[int(i) for i in input().split()]
for i in l:
	print(i, end=" ")#sep=" "
#or
print("\n")
print(*l,end=" ")
print()

'''
2 3 4 5 5 3 2 4 4 2 

2 3 4 5 5 3 2 4 4 2 
'''

