import re


numbers = input()
numbers_pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
results = re.finditer(numbers_pattern, numbers)

for result in results:
    print(result.group(), end=" ")