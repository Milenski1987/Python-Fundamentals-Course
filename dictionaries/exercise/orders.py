def create_products_data(products_data: dict, products_input: list) -> dict:
    product_name = products_input[0]
    product_price = float(products_input[1])
    product_quantity = int(products_input[2])

    if product_name not in products_data:
        products_data[product_name] = {}
        products_data[product_name]['price'] = 0
        products_data[product_name]['quantity'] = 0
    products_data[product_name]['price'] = product_price
    products_data[product_name]['quantity'] += product_quantity

    return products_data


def calculate_product_total_price(final_quantity: int, final_price: float) -> float:
    return final_quantity * final_price


def main():
    products = {}

    while True:
        product = input()

        if product == "buy":
            break

        current_product = product.split()
        products = create_products_data(products, current_product)

    for product in products.keys():
        quantity = products[product]['quantity']
        price = products[product]['price']
        total_price = calculate_product_total_price(quantity, price)
        print(f"{product} -> {total_price:.2f}")


main()