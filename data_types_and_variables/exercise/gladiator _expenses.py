lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_helm_breaks = lost_fights_count // 2
total_sword_breaks = lost_fights_count // 3
total_shield_breaks = lost_fights_count // (2 * 3)
total_armor_breaks = total_shield_breaks // 2

expenses = total_helm_breaks * helmet_price + \
           total_sword_breaks * sword_price + \
           total_shield_breaks * shield_price + \
           total_armor_breaks * armor_price


print(f"Gladiator expenses: {expenses:.2f} aureus")
