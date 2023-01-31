import menu

def calculate_tab(table):
    items = []
    for food in table:
        for product in menu.products:
            if (food['_id'] == product['_id']):
                items.append(product['price'] * food['amount'])
    subtotal = sum(items)
    return {'subtotal': f'${round(subtotal, 2)}'}