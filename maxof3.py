#Print Max of Three Numbers
a,b,c=[int(i) for i in input().split()]
if a>=c and a>=b:
    print(a)
elif b>=c and b>=a:
    print(b)
else:
    print(c)

'''
8 12 1
12
'''
