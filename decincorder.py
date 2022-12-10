# Check entered elemets are which order
a,b,c=[int(i) for i in input().split()]
if a>b>c:
    print("DEcrementing order")
elif a<b<c:
    print("Increment Order")
else:
    print("Unorder Elements are entered")
'''
3 6 8
Increment Order
'''
