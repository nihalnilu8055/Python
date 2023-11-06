def fun(a):
    b=[]
    b.append(a[0])
    b.append(a[1])
    b.append(a[-2])
    b.append(a[-1])
    for i in b:
        print(i,". ",end=" ")
a=input("enter a string: ")
fun(a)