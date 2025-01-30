repeat_string = lambda string, n: string * n

some_string = input()
counter = int(input())
result = repeat_string(some_string, counter)

print(result)