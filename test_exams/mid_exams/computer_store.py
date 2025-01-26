TAX = 0.20
SPECIAL_USER_DISCOUNT = 0.10

total_price = 0
special_customer = False

while True:
    command = input()

    if command == "special":
        special_customer = True
        break
    elif command == "regular":
        break

    price = float(command)

    if price < 0:
        print("Invalid price!")
        continue

    total_price += price

if total_price == 0:
    print("Invalid order!")

else:
    taxes = total_price * TAX
    total_price_with_taxes = total_price + taxes
    if special_customer:
        total_price_with_taxes -= total_price_with_taxes * SPECIAL_USER_DISCOUNT

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_with_taxes:.2f}$")