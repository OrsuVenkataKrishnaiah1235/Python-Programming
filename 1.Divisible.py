#1.Print a Number btween given range which divisible by the 7 but not divisible by the 5
#Answer sould be separated by comma
n,k=2,200
l=[]
for i in range(n,k+1):
	if(i%7==0 and i%5!=0):
		l.append(str(i))
print(",".join(l)) 


