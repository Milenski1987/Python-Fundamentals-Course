def positive_or_negative(num1, num2, num3):
    my_list = [num1, num2, num3]

    negative_nums = 0
    for num in my_list:
        if num == 0:
            return "zero"
        if num < 0:
            negative_nums += 1

    if negative_nums % 2 != 0:
        return "negative"
    else:
        return "positive"


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(positive_or_negative(first_number, second_number, third_number))

