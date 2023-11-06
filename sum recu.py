# def sum(n):
#     if n==0:
#         return 0
#     return n+sum(n-1)
# num=int(input("Enter a number: "))
# result=sum(num)
# print("Sum of num 0 to", num, "=", result)



a=0
def sum(n):
    if n>0:
        global a
        a+=n
        sum(n-1)
n=int(input("enter a number: "))
sum(n)
print("sum of the number:",a)        