import re

text = input()
email_pattern = r"(^|(?<=\s))[a-z0-9]+([\.|\-|\_][a-z0-9]+)?@[a-z]+([\-|\.][a-z]+)*\.[a-z]+"

results = re.finditer(email_pattern, text)

for result in results:
    print(result.group(), end= "\n")