class demo:
    #defining class attributes like variables
    hi="My WORLD"
    k="small gap"
    #defining class methods like functions
    def pr(self):
        print("Helllo ")
    def wi(self):
        print("Welcome")
#creating a object for demo class
my_demo=demo()
#accesing the attributes
print(my_demo.hi)
print(my_demo.k)
#accesing the methods
my_demo.pr()
my_demo.wi()

'''
My WORLD
small gap
Helllo 
Welcome
'''
