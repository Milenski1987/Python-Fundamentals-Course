import re

sentence = input()
searching_for = input()

pattern = fr"(?i)\b{searching_for}+\b"
results = re.findall(pattern,sentence)

print(len(results))