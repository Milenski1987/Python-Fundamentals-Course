def order_price(product, quantity):
    total_price = 0

    if product == "coffee":
        total_price = quantity * 1.50
    elif product == "water":
        total_price = quantity * 1.00
    elif product == "coke":
        total_price = quantity * 1.40
    elif product == "snacks":
        total_price = quantity * 2.00

    return f"{total_price:.2f}"


product_type = input()
product_quantity = int(input())

print(order_price(product_type,product_quantity))