#Print the Max Sum of Values
l={'a':[10,2,3,1212],'b':[11,2,3,1,2121],'c':[13,1,2,1231,23,1,2,1212]}
m=[]
for i in l.values():
    m.append(sum(i))
print(m)
print(max(m))

'''
[1227, 2138, 2485]
2485
'''
