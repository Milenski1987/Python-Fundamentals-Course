country_names = input().split(", ")
country_capitals = input().split(", ")

capitals = dict(zip(country_names, country_capitals))

for country, capital in capitals.items():
    print(f"{country} -> {capital}")