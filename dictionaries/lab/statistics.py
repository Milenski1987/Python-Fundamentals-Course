statistic = {}

while True:
    command = input()
    if command == "statistics":
        print("Products in stock:")
        for product, quantity in statistic.items():
            print(f"- {product}: {quantity}")
        print(f"Total Products: {len(statistic)}\nTotal Quantity: {sum(statistic.values())}")
        break

    product, quantity = command.split(": ")
    quantity = int(quantity)

    if product not in statistic:
        statistic[product] = 0
    statistic[product] += quantity