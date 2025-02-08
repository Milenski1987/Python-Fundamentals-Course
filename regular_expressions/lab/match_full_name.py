import re

names = input()
name_pattern = r"\b[A-Z][a-z]+ {1}[A-Z][a-z]+\b"

results = re.findall(name_pattern, names)

print(" ".join(results))