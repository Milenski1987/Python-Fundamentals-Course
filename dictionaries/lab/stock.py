product_data = input().split()
products = {}
searching_for = input().split()

for index in range(0, len(product_data), 2):
    products[product_data[index]] = int(product_data[index + 1])

for product in searching_for:
    if product in products.keys():
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")