#Generate all Permutations of a List ()
import itertools
l=[1,2,3]
permutations=list(itertools.permutations(l))


for i in permutations:
	print(i)
'''
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
'''
