items_list = input().split("|")
budget = float(input())
bought_items = []
profit = 0
train_to_france = 150

for item in items_list:
    current_item, price = item.split("->")
    price = float(price)
    if (current_item == "Clothes" and price <= 50.00) \
            or (current_item == "Shoes" and price <= 35.00) \
            or (current_item == "Accessories" and price <= 20.50):
        if budget >= price:
            budget -= price
            selling_price = price * 1.4
            profit += selling_price - price
            bought_items.append(f"{selling_price:.2f}")

print(*bought_items)
print(f"Profit: {profit:.2f}")
if budget + sum([float(price) for price in bought_items]) >= train_to_france:
    print("Hello, France!")
else:
    print("Not enough money.")