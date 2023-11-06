num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))
while num2:
    num1,num2=num2,num1%num2
gcd=num1
print(gcd)    




# num1 = 36
# num2 = 60
# a = num1
# b = num2

# while num1 != num2:
#     if num1 > num2:
#         num1 -= num2
#     else:
#         num2 -= num1

# print("GCD of", a, "and", b, "is", num1)