
import resto as menu

print("Menu:")
for item, price in menu.menu_list.items():
    print(f"{item}: ${price}")

order = []
while True:
    item = input("Enter an item name (or 'q' to quit): ")
    if item == 'q':
        break
    order.append(item)

total_cost = 0
for item in order:
    total_cost += menu.get_price(item)

print(f"Total cost: ${total_cost}")
