employee_happiness = [int(number) for number in input().split()]
factor = int(input())

improved_happiness = list(map(lambda x: employee_happiness[x] * factor, range(len(employee_happiness))))

average_happiness = sum(improved_happiness) / len(improved_happiness)

result = list(filter(lambda x: x > average_happiness, improved_happiness))

if len(result) >= len(improved_happiness) / 2:
    print(f"Score: {len(result)}/{len(improved_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(result)}/{len(improved_happiness)}. Employees are not happy!")