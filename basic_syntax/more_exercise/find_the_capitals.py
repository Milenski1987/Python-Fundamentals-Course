string = input()
capital_letters_idx = []

for index, character in enumerate(string):
    if character.isupper():
        capital_letters_idx.append(index)

print(capital_letters_idx)