class student:
    def __init__(self,Name,RollNo,Class):
        self.Name=Name
        self.RollNo=RollNo
        self.Class=Class
    def details(self):
        return self.Name
college=student("Krishna",170452,20)
print(college.details())
print(college.Name)
print(college.RollNo)
print(college.Class)

'''
Krishna
Krishna
170452
20
'''
