def add(a,b):
    result=a+b
    print(result)
def sub(a,b):
    result=a-b
    print(result)
def mul(a,b):
    result=a*b
    print(result)
def div(a,b):
    result=a/b
    print(result)
print("select any")
print("1. add")
print("2. sub")
print("3. mul") 
print("4. div")

select=input("select any 1 to 4: ")

num1=int(input("enter 1st num: "))
num2=int(input("enter 2nd num: "))
if select =='1':
    add(num1,num2)
    
elif select=='2':
    sub(num1,num2)
elif select=='3':
    mul(num1,num2)
elif select=='4':
    div(num1,num2)
else:
    print("error")




# def add(x, y):
#     print(x + y)

# def subtract(x, y):
#     print(x - y)

# def multiply(x, y):
#     print(x * y)

# def divide(x, y):
#     if y != 0:
#         print(x / y)
#     else:
#         print("Cannot divide by zero")

# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = input("Enter choice (1/2/3/4): ")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if choice == '1':
#     print("Result:", end=" ")
#     add(num1, num2)
# elif choice == '2':
#     print("Result:", end=" ")
#     subtract(num1, num2)
# elif choice == '3':
#     print("Result:", end=" ")
#     multiply(num1, num2)
# elif choice == '4':
#     print("Result:", end=" ")
#     divide(num1, num2)
# else:
#     print("Invalid input")
