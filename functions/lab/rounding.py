initial_list = [float(number) for number in input().split()]
rounded_list = []

for number in initial_list:
    rounded_list.append(round(number))

print(rounded_list)