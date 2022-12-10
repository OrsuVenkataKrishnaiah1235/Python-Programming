# Simple Calculator
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def adition(self):
        print("Addition",self.a+self.b)
    def Subtract(self):
        print("Substract",self.a-self.b)
    def mul(self):
        print("Multiflication",self.a*self.b)
    def Div(self):
        print("Divition",self.a/self.b)
    def Modulo(self):
        print("Modulo",self.a%self.b)
a=int(input("Enter the number "))
b=int(input("Enter the number "))
c=calculator(a,b)
c.adition()
c.Subtract()
c.mul()
c.Div()
c.Modulo()



'''
Enter the number 6
Enter the number 3
Addition 9
Substract 3
Multiflication 18
Divition 2.0
Modulo 0
'''
