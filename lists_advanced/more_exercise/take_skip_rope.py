initial_string = input()

digits_list = []
non_digits_list = []

for character in initial_string:
    if character.isdigit():
        digits_list.append(character)
    else:
        non_digits_list.append(character)

take_list = []
skip_list = []
for index in range(len(digits_list)):
    if index % 2 == 0:
        take_list.append(digits_list[index])
    else:
        skip_list.append(digits_list[index])

result_string = ""
for i in range(len(take_list)):
    take_chars = int(take_list[i])
    skip_chars = int(skip_list[i]) + take_chars
    result_string += "".join(non_digits_list[:take_chars])
    non_digits_list = non_digits_list[skip_chars:]

print(result_string)