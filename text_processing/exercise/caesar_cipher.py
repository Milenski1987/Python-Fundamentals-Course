def encrypt_text(some_string: str) -> str:
    result_text = ""
    for character in some_string:
        result_text += chr(ord(character) + 3)
    return result_text


def main():
    text = input()
    encrypted_text = encrypt_text(text)

    print(encrypted_text)


main()