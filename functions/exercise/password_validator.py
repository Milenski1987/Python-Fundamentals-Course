def length_validation(current_password: str) -> bool:
    if len(current_password) in range(6, 11):
        return True
    return False


def letters_digits_validation(current_password: str) -> bool:
    if current_password.isalnum():
        return True
    return False


def digits_count_validation(current_password: str) -> bool:
    digits_count = 0
    for character in current_password:
        if character.isdigit():
            digits_count += 1
    if digits_count >= 2:
        return True
    return False


def password_validation(current_password: str) -> str:
    password_statement = ""

    if length_validation(current_password) and letters_digits_validation(current_password) and digits_count_validation(current_password):
        password_statement += "Password is valid"

    if not length_validation(current_password):
        password_statement += "Password must be between 6 and 10 characters\n"

    if not letters_digits_validation(current_password):
        password_statement += "Password must consist only of letters and digits\n"

    if not digits_count_validation(current_password):
        password_statement += "Password must have at least 2 digits\n"

    return password_statement



password = input()
result = password_validation(password)

print(result)
