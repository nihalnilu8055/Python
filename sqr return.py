# def sqr(n):
#     return sum(i**2 for i in range(1,n+1))
# print(sqr(5))



def sqr(n):
    total=0
    i=1
    while i<=n:
        total+=i**2
        i+=1
    return total
print (sqr(2))