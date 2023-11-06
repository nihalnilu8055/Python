num1=int(input("enter 1st number "))
num2=int(input("enter 2nd number "))
num3=int(input("enter 3rd number "))
if num1>num2 and num2>num3:
    print(num1+num2)
elif num2>num3 or num3>num1:
    print(num2+num3)
else:
    print(num1+num3)