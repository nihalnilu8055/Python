# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# num=int(input("Enter a number: "))
# result=fact(num)
# print("Fact of", num, "=", result)



a=1
def fact(n):
    if n>0:
        global a
        a*=n
        fact(n-1)
n=int(input("Enter a number: "))
fact(n)
print("sum of the numb:",a)      