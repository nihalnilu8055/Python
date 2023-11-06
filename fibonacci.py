limit= int(input("enter a number: "))
fib=[0,1]

for i in range(2,limit):
    fib1=fib[-1] + fib[-2]
    if fib1<=limit:
        fib.append(fib1)
    else:
        break

for num in fib:
    print(num,end=" ")  