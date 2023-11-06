balance=float(input("enter ur account balance: "))
option=input("withdraw or deposit?(w/d):")
if option=="w":
    amount=float(input("enter ur amount: "))
    balance-=amount
elif option=="d":
    amount=float(input("enter ur amount: "))
    balance+=amount
print("balance is: ",balance)
