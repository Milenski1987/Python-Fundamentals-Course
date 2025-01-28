strings_count = int(input())
word = input()

some_strings = []

for _ in range(strings_count):
    some_string = input()
    some_strings.append(some_string)

print(some_strings)
some_strings = [element for element in some_strings if word in element]
print(some_strings)