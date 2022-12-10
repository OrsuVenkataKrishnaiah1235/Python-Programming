import math
#Solve Quadratic Equations
a,b,c=2,14,7
dicriminate=(b**2)-(4*a*c)
if dicriminate<0:
    print("Complex Roots")
elif dicriminate==0:
    r=-b/(2*a)
    print(r)
else:
    r1=(-b-math.sqrt(dicriminate)/(2*a))
    r2=(-b+math.sqrt(dicriminate)/(2*a))
    print(r1,r2)

#-16.95803989154981 -11.041960108450192

