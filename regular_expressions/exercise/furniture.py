import re


pattern = r">>([A-Za-z]+)<<([0|1-9]?[0-9]+\.?[0-9]*)!([0-9]+)"
furniture = []
total_cost = 0
while True:
    command = input()

    if command == "Purchase":
        break

    bought_items = re.search(pattern, command)

    if bought_items:
        name, price, quantity = bought_items.groups()

        furniture.append(name)
        total_cost += float(price) * int(quantity)

print("Bought furniture:")
for current_furniture in furniture:
    print(current_furniture)
print(f"Total money spend: {total_cost:.2f}")
