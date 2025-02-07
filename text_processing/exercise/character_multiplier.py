def calculate_total_sum(string1: str, string2: str) -> int:
    total_sum = 0

    if len(string1) > len(string2):
        for index in range(len(string2)):
            total_sum += ord(string1[index]) * ord(string2[index])
        for index in range(len(string2), len(string1)):
            total_sum += ord(string1[index])
    elif len(string1) < len(string2):
        for index in range(len(string1)):
            total_sum += ord(string1[index]) * ord(string2[index])
        for index in range(len(string1), len(string2)):
            total_sum += ord(string2[index])
    else:
        for index in range(len(string1)):
            total_sum += ord(string1[index]) * ord(string2[index])
    return total_sum

def main():
    first_string, second_string = input().split()

    final_sum = calculate_total_sum(first_string, second_string)

    print(final_sum)


main()