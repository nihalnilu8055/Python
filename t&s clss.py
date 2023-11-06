class school:
    def __init__(self,name,dept):
        self.na=name
        self.dep=dept
    def teacher(self):
        print(self.na)
        print(self.dep)
        print("salary is 10000")
    def student(self):
        print(self.na)
        print(self.dep)
        print("enrollment number is 8055")
name=input("enter ur name: ")
dept=input("enter ur dept: ")
obj=school(name,dept)
obj.teacher()
obj.student()