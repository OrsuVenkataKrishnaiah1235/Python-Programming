def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
a=int(input("Enter the number"))
m=fact(a)
print("Factorial Of number",m)
