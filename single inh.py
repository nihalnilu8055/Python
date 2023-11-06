# class vehicle:
#     def start_eng(self):
#         print("the engi is start")
# class car(vehicle):
#     def drive(self):
#         print("the car is driving")
# obj=car()
# obj.start_eng()
# obj.drive()




# class empl:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary 
#         print(self.name,self.salary) 
# class mang(empl):
#     def __init__(self, name, salary,dept):
#         self.dept=dept
#     def dis(self,a):
#         self.a=a 
#         print(self.a)        

# ob = mang("abc",10000,"cs") 
# ob.dis(10) 
# ob1 = empl("ccc",50000)




class shape:
    def __init__(self,color,size):
        self.color=color
        self.size=size
class circle(shape):
    def __init__(self,color,size,radius):
        self.radius=radius        