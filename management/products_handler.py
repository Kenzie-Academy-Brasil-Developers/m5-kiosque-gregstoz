from menu import products
from collections import Counter

def get_product_by_id(id):
    if type(id) != int:
        raise TypeError("product id must be an int")
    for item in products:
        if item["_id"] == id:
            return item
    return {}


def get_products_by_type(item_type):
    if type(item_type) != str:
        raise TypeError("product type must be a str")
    prods = []
    for prod in products:
        if prod["type"] == item_type:
            prods.append(prod)
    return prods


def add_product(menu, **args):
    product = args
    if len(menu) == 0:
        product["_id"] = 1
        return product
    ids = []
    for menu_ids in menu:
        ids.append(menu_ids["_id"])
    ids.sort()
    product["_id"] = ids[-1] + 1
    return product
        

def menu_report():
    average_prices = []
    for prod in products:
        average_prices.append(prod["price"])
    
    prices = 0
    for media_price in average_prices:
        prices += media_price
    
    media = prices / len(average_prices)

    types = []
    for type in products:
        types.append(type["type"])
    
    types_counter = Counter(types)
    types_tuple = tuple(types_counter)

    menu = f"Products Count: {len(products)} - Average Price: {media} - Most Common Type: {types_tuple[0]}"

    return menu
