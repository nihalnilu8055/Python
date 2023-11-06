age=int(input("enter ur age  "))
day=input("enter day  ")
age=12
age1=18
age2=65
if age<12 or age2>65:
    print("ticket rate is 5")
elif age>=12 or age1 <=18 and day == "wed":
    print("4")
else:
    print("ticket rate is 10")