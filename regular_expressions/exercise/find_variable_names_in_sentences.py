import re

variables = []
some_string = input()
variables_pattern = r"\b_([A-Za-z0-9]+)\b"

results = re.findall(variables_pattern, some_string)
for result in results:
    variables.append(result)

print(",".join(variables))

