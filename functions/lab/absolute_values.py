numbers_list = [float(number) for number in input().split()]
absolute_value_list = []

for number in numbers_list:
    absolute_value_list.append(abs(number))

print(absolute_value_list)
