def get_name_and_extension(file_info: str) -> tuple:
    name, extension = file_info.split(".")
    return name, extension


def main():
    file_path = input().split("\\")

    file_information = file_path[-1]
    file_name, file_extension = get_name_and_extension(file_information)

    print(f"File name: {file_name}\nFile extension: {file_extension}")


main()