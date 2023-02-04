n=int(input("enter the number "))
for num in range(2,n):
    for i in range(2,num):
        if(num%2==0):
            break
        else:
            print(num,end=" ")
print()
