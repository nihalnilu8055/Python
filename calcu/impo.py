import calcu as cal

print("select any")
print("1. add")
print("2. sub")
print("3. mul") 
print("4. div")
select=input("select any 1 to 4: ")
num1=int(input("enter 1st num: "))
num2=int(input("enter 2nd num: "))

if select =='1':
    cal.add(num1,num2)
elif select=='2':
    cal.sub(num1,num2)
elif select=='3':
    cal.mul(num1,num2)
elif select=='4':
    cal.div(num1,num2)
else:
    print("error")