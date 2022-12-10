#check leaf year or not
n=int(input("Enter the year"))
if(n%4==0 or(n%100==0 and n%400==0)):
    print("Leaf year")
else:
    print("Not a leaf year")
