#Count Repeated Characters ()
n=input("Enter the String ")
di=dict()
for i in n:
	m=n.count(i)
	di[i]=m
print(di)

'''
print(i,m)
Enter the String"Krishnaiah"
('K', 1)
('r', 1)
('i', 2)
('s', 1)
('h', 2)
('n', 1)
('a', 2)
('i', 2)
('a', 2)
('h', 2)

Enter the String "Krishnaiah"
{'a': 2, 'i': 2, 'h': 2, 'K': 1, 'n': 1, 's': 1, 'r': 1}

'''
