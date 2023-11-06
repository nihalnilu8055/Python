class calcu():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
obj=calcu(a,b)
choice=1
print("1. Add")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("0. Exit")
choice=int(input("Enter choice: "))
if choice==1:
    print(obj.add())
elif choice==2:
    print(obj.sub())
elif choice==3:
    print(obj.mul())
elif choice==4:
    print(obj.div)
elif choice==0:
    print("Exiting!")
else:
    print("Invalid choice!!")
print()