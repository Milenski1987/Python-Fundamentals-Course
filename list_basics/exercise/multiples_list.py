factor = int(input())
count = int(input())

numbers_list = []

for i in range(1, count + 1):
    number = factor * i
    numbers_list.append(number)

print(numbers_list)