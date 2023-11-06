menu = {
    "burger":30,
    "pizza":50,
    "biriyani":100,
}

def add_item(item, price):
    menu[item] = price

def remove_item(item):
    del menu[item]

def get_price(item):
    return menu[item]


