def create_products_data(products_dictionary: dict, products_list: list) -> dict:
    for index in range(0, len(products_list), 2):
        products_dictionary[products_list[index]] = int(products_list[index + 1])
    return products_dictionary

def check_product_availability(products_dictionary: dict, current_product: str) -> str:
        if current_product in products_dictionary.keys():
            return f"We have {products_dictionary[current_product]} of {current_product} left"
        return f"Sorry, we don't have {current_product}"


product_data = input().split()
searching_for = input().split()

products = {}
products = create_products_data(products, product_data)

for product in searching_for:
    result = check_product_availability(products, product)

    print(result)