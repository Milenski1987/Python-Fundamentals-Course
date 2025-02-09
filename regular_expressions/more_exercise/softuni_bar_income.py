import re

pattern = r"\%([A-Z][a-z]+)\%[^\|\$\%\.]*?\<(\w+)\>[^\|\$\%\.]*?\|([0-9]+)\|[^\|\$\%\.]*?([0-9.]+[0-9])\$"
total_income = 0

while True:
    command = input()

    if command == "end of shift":
        break

    result = re.findall(pattern, command)

    if result:
        name = result[0][0]
        product = result[0][1]
        quantity = int(result[0][2])
        price = float(result[0][3])
        income = quantity * price
        total_income += income

        print(f"{name}: {product} - {income:.2f}")

print(f"Total income: {total_income:.2f}")

