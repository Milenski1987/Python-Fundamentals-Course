import re
def encrypting_message(message: str) -> str:
    encrypted_message = ""
    pattern = r"(?i)([star])"
    results = re.findall(pattern, message)
    counter = len(results)

    for character in message:
        encrypted_message += chr(ord(character) - counter)

    return encrypted_message


def find_planet(message: str, attacked: list, destroyed: list) -> str:
    planet_pattern = r"@([A-Za-z]+)[^\@\-\!\:\>]*\:([\d]+)[^\@\-\!\:\>]*\!([A|D])\![^\@\-\!\:\>]*->([\d]+)"
    result = re.findall(planet_pattern, message)

    if result:
        planet_name = result[0][0]
        planet_population = int(result[0][1])
        planet_attack_type = result[0][2]
        planet_soldier_count = int(result[0][3])

        if planet_attack_type == "A":
            attacked.append(planet_name)
        elif planet_attack_type == "D":
            destroyed.append(planet_name)

    return attacked, destroyed


def main():
    number_of_messages = int(input())
    attacked_planets = []
    destroyed_planets = []
    for _ in range(number_of_messages):
        current_message = input()

        current_encrypted_message = encrypting_message(current_message)
        attacked_planets, destroyed_planets = find_planet(current_encrypted_message, attacked_planets, destroyed_planets)


    print(f"Attacked planets: {len(attacked_planets)}")
    if attacked_planets:
        attacked_planets = sorted(attacked_planets)
        for planet in attacked_planets:
            print(f"-> {planet}")
    print(f"Destroyed planets: {len(destroyed_planets)}")
    if destroyed_planets:
        destroyed_planets = sorted(destroyed_planets)
        for planet in destroyed_planets:
            print(f"-> {planet}")


main()