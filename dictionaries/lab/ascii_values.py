characters_list = input().split(", ")
characters = {character: ord(character) for character in characters_list}

print(characters)