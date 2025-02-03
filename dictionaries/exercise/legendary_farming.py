materials = {"shards": 0, "fragments": 0, "motes": 0}
key_materials = ["shards", "fragments", "motes"]
obtained_item = ""
obtained = False

while True:
    loot = input().split()
    for index in range(0, len(loot), 2):
        quantity = int(loot[index])
        material = loot[index + 1].lower()

        if material not in materials:
            materials[material] = 0
        materials[material] += quantity

        if materials[material] >= 250 and material in key_materials:
            if material == "shards":
                obtained_item = "Shadowmourne"
                materials[material] -= 250
            elif material == "fragments":
                obtained_item = "Valanyr"
                materials[material] -= 250
            elif material == "motes":
                obtained_item = "Dragonwrath"
                materials[material] -= 250

        if obtained_item:
            obtained = True
            break

    if obtained:
        break

print(f"{obtained_item} obtained!")
for material in key_materials:
    print(f"{material}: {materials[material]}")
for material, quantity in materials.items():
    if material not in key_materials:
        print(f"{material}: {quantity}")