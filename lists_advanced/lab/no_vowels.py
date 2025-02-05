some_string = input()
vowels = ["a", "o", "u", "e", "i"]
result_string = [character for character in some_string if character.lower() not in vowels]

print("".join(result_string))