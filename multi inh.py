# class a:
#     def display(self):
#         print("hiii")
# class b:
#     def sample(self):
#         print("hloo")
# class c(a,b):
#     def demo(self):
#         print("koiiii")

# obj=c()
# obj.display()
# obj.sample()
# obj.demo()




class animal:
    def __init__(self,name):
        self.name=name
class canfly:
    def fly(self):
        pass
class canswim:
    def swim(self):
        pass
class duck(animal,canfly,canswim):
    def __init__(self, name,color):
        self.color=color                