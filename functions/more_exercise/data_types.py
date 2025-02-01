def type_int() -> int:
    number = int(input())
    return number * 2


def type_real() -> str:
    number = float(input())
    return f"{(number * 1.5):.2f}"


def type_string() -> str:
    some_string = input()
    result_string = "$" + some_string + "$"
    return result_string

def main():
    data_type = input()
    result = None

    if data_type == "int":
        result = type_int()

    elif data_type == "real":
        result = type_real()

    elif data_type == "string":
        result = type_string()

    print(result)

main()

