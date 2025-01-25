def length_validation(word):
    if len(word) in range(6, 11):
        return True
    return False


def letters_digits_validation(word):
    if word.isalnum():
        return True
    return False


def digits_count_validation(word):
    digits_count = 0

    for character in word:
        if character.isdigit():
            digits_count += 1

    if digits_count >= 2:
        return True
    return False


password = input()
length_validation(password)

if length_validation(password) and letters_digits_validation(password) and digits_count_validation(password):
    print("Password is valid")

if not length_validation(password):
    print("Password must be between 6 and 10 characters")

if not letters_digits_validation(password):
    print("Password must consist only of letters and digits")

if not digits_count_validation(password):
    print("Password must have at least 2 digits")
