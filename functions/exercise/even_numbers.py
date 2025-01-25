def even(num):
    return num % 2 == 0


numbers = [int(number) for number in input().split()]
result = list(filter(even, numbers))

print(result)

