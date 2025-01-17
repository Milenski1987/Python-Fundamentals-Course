number_of_snowballs = int(input())
max_snowball_value = 0
result = ""

for snowball in range(number_of_snowballs):
    weight = int(input())
    time_to_target = int(input())
    quality = int(input())

    snowball_value = int((weight / time_to_target) ** quality)
    if snowball_value > max_snowball_value:
        max_snowball_value = snowball_value
        result = f"{weight} : {time_to_target} = {snowball_value} ({quality})"

print(result)