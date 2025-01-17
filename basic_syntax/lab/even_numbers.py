number_of_lines = int(input())

for _ in range(number_of_lines):
    number = int(input())

    if number % 2 != 0:
        print(f"{number} is odd!")
        break

else:
    print("All numbers are even.")