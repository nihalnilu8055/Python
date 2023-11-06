pin=1234
balanace=0

# def pin(attempts=3):
#     c_pin="1234"
#     while attempts>0:
#         input=input("enter ur pin: ")
#         if input==c_pin:
#             print("pin verified")
#             return True
#         else:
#             attempts-=1
#             if attempts>0:
#                 print("incorrect pin")
#             else:
#                 print("no more try")
#                 return False    
            
def deposit():
    d=int(input("enter ur deposit amount: "))
    global balanace
    balanace+=d
    print("ur balance is ",balanace)
    print("\nATM Options:")
    print("1. Display Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    ls = input("Enter your choice (1/2/3/4): ")
    if ls=="1":
        balu()
    elif ls=="2":
        withdraw()
    elif ls=="3":
        deposit()
    elif ls=="4":
        exit()

def withdraw():
    global balanace
    w=int(input("enter ur withdraw amount: "))
    if balanace>w:
        balanace-=w
    else:
        print("u dont have enough balance")
    print("ur current balance",balanace)
    
    print("\nATM Options:")
    print("1. Display Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")        
    ls = input("Enter your choice (1/2/3/4): ")
    if ls=="1":
        balu()
    elif ls=="2":
        withdraw()
    elif ls=="3":
        deposit()
    elif ls=="4":
        exit()
    
def balu():
    global balanace
    print("ur current balance",balanace)
    print("\nATM Options:")
    print("1. Display Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    
    
    ls = input("Enter your choice (1/2/3/4): ")
    if ls=="1":
        balu()
    elif ls=="2":
        withdraw()
    elif ls=="3":
        deposit()
    elif ls=="4":
        exit()
    
for i in range(1):
    a=int(input("enter ur pin: "))
    if a==pin:
        print("\nATM Options:")
        print("1. Display Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        ls = input("Enter your choice (1/2/3/4): ")
        if ls=="1":
         balu()
        elif ls=="2":
            withdraw()
        elif ls=="3":
            deposit()
        elif ls=="4":
            exit()
    else:
        a!=pin
        a=input("re enter ur pin: ")
        if a==pin:
            print("\nATM Options:")
            print("1. Display Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")
            ls = input("Enter your choice (1/2/3/4): ")
            if ls=="1":
                balu()
            elif ls=="2":
                withdraw()
            elif ls=="3":
                deposit()
            elif ls=="4":
                exit()
        else:
            print("no more try!!!!")
