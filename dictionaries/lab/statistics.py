def statistics_command(statistics_dictionary) -> str:
    result = "Products in stock:\n"
    for product, quantity in statistics_dictionary.items():
        result += f"- {product}: {quantity}\n"
    result += f"Total Products: {len(statistics_dictionary)}\nTotal Quantity: {sum(statistics_dictionary.values())}"
    return result


def dictionary_creation(statistics_dictionary: dict, current_product: str, product_quantity: int) -> dict:
    if current_product not in statistics_dictionary:
        statistics_dictionary[current_product] = 0
    statistics_dictionary[current_product] += product_quantity
    return statistics_dictionary

def main():
    statistic = {}

    while True:
        command = input()
        if command == "statistics":
            final_result = statistics_command(statistic)
            print(final_result)
            break

        product, quantity = command.split(": ")
        quantity = int(quantity)

        statistic = dictionary_creation(statistic, product, quantity)


main()