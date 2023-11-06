add=lambda x,y:x+y
sub=lambda x,y:x-y
mul=lambda x,y:x*y
div=lambda x,y:x/y

print("select any")
print("1. add")
print("2. sub")
print("3. mul") 
print("4. div")

select=input("select any 1 to 4: ")
num1=int(input("enter 1st num: "))
num2=int(input("enter 2nd num: "))

if select =='1':
    result=add(num1,num2)
    print("result",result) 
elif select=='2':
    result=sub(num1,num2)
    print("result",result)
elif select=='3':
    result=mul(num1,num2)
    print("result",result)
elif select=='4':
    result=div(num1,num2)
    print("result",result)
else:
    print("error")