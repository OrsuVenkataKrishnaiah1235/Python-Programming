#Remove Duplicates from a List
l=[int(i) for i in input().split()]
print(list(set(l)))
print(list(dict.fromkeys(l)))

'''
2 3234  34 12 3 2 212 33 4 45233 2 2 3 44 5 24535 
[33, 3234, 2, 3, 34, 4, 5, 12, 44, 45233, 212, 24535]
[2, 3234, 34, 12, 3, 212, 33, 4, 45233, 44, 5, 24535]
'''
