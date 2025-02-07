def check_username_validity(user: str) -> str:
    if check_username_length(user) and check_username_contains(user) and check_for_redundant(user):
        return user
    return ""


def check_username_length(user: str) -> bool:
    if len(user) in range(3, 17):
        return True
    return False


def check_username_contains(user: str) -> bool:
    valid = True
    for character in user:
        if character.isalnum() or character == "-" or character == "_":
            continue
        else:
            valid = False
            break
    return valid


def check_for_redundant(user: str) -> bool:
    valid = True
    if user.startswith(" ") or user.endswith(" "):
        valid = False
    return valid


def main():
    usernames = input().split(", ")

    for name in usernames:
        result = check_username_validity(name)
        if result:
            print(result)


main()


