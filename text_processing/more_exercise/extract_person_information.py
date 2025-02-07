import re


name_pattern = r"\@([A-Za-z]+)\|"
age_pattern = r"\#([0-9]+)\*"

number_of_strings = int(input())

for _ in range(number_of_strings):
    some_string = input()
    name = re.findall(name_pattern, some_string)[0]
    age = re.findall(age_pattern, some_string)[0]

    print(f"{name} is {age} years old.")