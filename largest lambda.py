large=lambda x,y: x if x>=y else y
num1=int(input("enter the 1st num: "))
num2=int(input("enter the 2nd num: "))
result=large(num1,num2)
print("large num is:",result)