def even_index(numbers_list: list) -> list:
    result_list = []
    for index in range(len(numbers_list)):
        if numbers_list[index] % 2 == 0:
            result_list.append(index)
    return result_list


numbers = [int(number) for number in input().split(", ")]
indices = even_index(numbers)

print(indices)