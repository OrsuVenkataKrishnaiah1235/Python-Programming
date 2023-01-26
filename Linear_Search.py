n=int(input("Enter the Key want to search "))
k=[int(i) for i in input().split()]
for j in range(0,len(k)):
    if k[j]==n:
        print("{0} Find at the position {1} ".format(k[j],j))
print()
'''
Enter the Key want to search 12
12 12 133 21232 123432
12Find at the position 0 
12Find at the position 1 '''