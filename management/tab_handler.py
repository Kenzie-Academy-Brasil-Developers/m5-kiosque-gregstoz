from menu import products

def calculate_tab(table):
    product = []
    for item in products:
        for table_item in table:
            if item["_id"] == table_item["_id"]:
                product.append(item)
    product_value = []
    for prod_value in product:
        product_value.append(prod_value["price"])
    result = []
    amount = []
    for table_amount in table:
        amount.append(table_amount["amount"])
    amount_values = len(product_value)
    for i in range(amount_values):
        result.append(product_value[i] * amount[i])
    subtotal = 0
    for count in result:
        subtotal += count
    return {"subtotal": round(subtotal, 2)} 