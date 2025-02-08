import re


phone_numbers = input()
phone_number_pattern = r"(\+359([\s\-])2\2[0-9]{3}\2[0-9]{4}\b)"

results = re.findall(phone_number_pattern, phone_numbers)
phones = []
for result in results:
    phones.append(result[0])

print(", ".join(phones))