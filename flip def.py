# def menu():
#     print("WELCOME TO ........")
#     print("1. shirt")
#     print("2. pants")
#     print("3. accessories")
#     print("4. show cart")
#     print("5. check out")
#     print("6. exit")

# def rate():
#     shirt=800
#     pants=1200
#     accessories=500
#     c=[]

#     while True:
#         menu()
#         choice=int(input("enter ur choice(1/2/3/4/5/6):"))

#         if choice==1:
#             c.append("shirt")
#             print("add shirt to cart")
#         elif choice==2:
#             c.append("pants")
#             print("add pants to cart")
#         elif choice==3:
#             c.append("accessories")
#             print("add accessories to cart")
#         elif choice==4:
#             print("items in cart ", ",".join(c))
#         elif choice==5:
#             total=len(c)*(shirt+pants+accessories)
#             print("ur total",total)
#             break
#         elif choice==6:
#             print("thnk u")
#             break
#         else:
#             print("invalid")
# rate() 







def buy_shirt(cart):
    cart.append(("Shirt", 500))
    print("Added Shirt to cart.")

def buy_pants(cart):
    cart.append(("Pants", 800))
    print("Added Pants to cart.")

def buy_accessories(cart):
    cart.append(("Accessories", 500))
    print("Added Accessories to cart.")

def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Items in cart:")
        for item, price in cart:
            print(f"{item}: ${price}")

def calculate_total(cart):
    
    total=sum(price for _, price in cart)
    if total>2000:
        total-=500
    print("Your total: $", total)

def main():
    cart=[]
    
    while True:
        print("Welcome to Flipkart...")
        print("1. Buy Shirt - $500")
        print("2. Buy Pants - $800")
        print("3. Buy Accessories - $500")
        print("4. Show Cart")
        print("5. Calculate Total")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            buy_shirt(cart)
        elif choice == 2:
            buy_pants(cart)
        elif choice == 3:
            buy_accessories(cart)
        elif choice == 4:
            display_cart(cart)
        elif choice == 5:
            calculate_total(cart)
        elif choice == 6:
            print("Thank you for visiting")
            break
        else:
            print("Please select a valid option.")

main()