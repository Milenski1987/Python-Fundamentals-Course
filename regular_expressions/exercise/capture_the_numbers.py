import re


numbers_pattern = r"\d+"
numbers = input()
result_list = []
while numbers:
    results = re.findall(numbers_pattern, numbers)
    for result in results:
        result_list.append(result)
    numbers = input()

print(" ".join(result_list))