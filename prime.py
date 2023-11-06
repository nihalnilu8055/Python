num=int(input("enter a number: "))
count=0
for i in range(1,11):
    if num%i==0 or num==1:
        count+=1
print("")
if count>2:
    print(num,"is not prime")
else:
    print(num,"is a prime")            