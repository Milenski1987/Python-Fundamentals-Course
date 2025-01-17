first_integer = int(input())
second_integer = int(input())
print("Before:")
print(f"a = {first_integer}\nb = {second_integer}")

first_integer, second_integer = second_integer, first_integer
print("After:")
print(f"a = {first_integer}\nb = {second_integer}")