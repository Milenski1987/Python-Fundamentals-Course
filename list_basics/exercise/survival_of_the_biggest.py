numbers_list = [int(number) for number in input().split()]
numbers_to_remove_count = int(input())

reformated_list = numbers_list.copy()
reformated_list.sort()
reformated_list = reformated_list[numbers_to_remove_count:]

for index in range(len(numbers_list) - 1, -1, -1):
    if numbers_list[index] not in reformated_list:
        numbers_list.remove(numbers_list[index])

print(*numbers_list, sep=", ")
