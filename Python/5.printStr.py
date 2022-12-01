class String:
    def __init__(self):
        self.s=""
    def getstring(self):
        self.s=input("Enter the string")
    def printstring(self):
        print(self.s.upper())
k=String()
k.getstring()
k.printstring()
