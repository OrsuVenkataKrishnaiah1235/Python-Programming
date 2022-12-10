#Print Min of Three Numbers
a,b,c=[int(i) for i in input().split()]
if(a<=b and a<=c):
    print(a)
elif(c<=a and c<=b):
    print(c)
else:
    print(b)
