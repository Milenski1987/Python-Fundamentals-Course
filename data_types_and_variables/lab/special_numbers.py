n = int(input())
special_sum = [5, 7, 11]

for number in range(1, n + 1):
    digits = [int(num) for num in str(number)]
    special_number = True
    if sum(digits) in special_sum:
        special_number = True
    else:
        special_number = False
    print(f"{number} -> {special_number}")