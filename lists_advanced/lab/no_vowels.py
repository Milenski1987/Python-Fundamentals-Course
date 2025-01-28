initial_string = list(input())
vowels = ["a", "o", "u", "e", "i"]
result_string = [character for character in initial_string if character.lower() not in vowels]

print("".join(result_string))