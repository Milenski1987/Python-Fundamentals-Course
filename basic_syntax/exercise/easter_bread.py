egg_pack_per_loaf = 1
flour_kg_per_loaf = 1
milk_liters_per_loaf = 0.250

colored_eggs = 0
loaves_count = 0

budget = float(input())
flour_kg_price = float(input())

egg_pack_price = flour_kg_price * 0.75
milk_liter_price = flour_kg_price * 1.25
price_per_loaf = egg_pack_per_loaf * egg_pack_price + flour_kg_per_loaf * flour_kg_price + milk_liters_per_loaf * milk_liter_price

while True:
    if budget - price_per_loaf >= 0:
        budget -= price_per_loaf
        loaves_count += 1
        colored_eggs += 3

        if loaves_count % 3 == 0:
            colored_eggs -= loaves_count - 2

    else:
        break

print(f"You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
