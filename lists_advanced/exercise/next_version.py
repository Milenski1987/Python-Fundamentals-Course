def find_next_version(version: list) -> list:
    initial_version = "".join(version)
    updated_version = int(initial_version) + 1
    return list(str(updated_version))


current_version = input().split(".")
result = find_next_version(current_version)

print(".".join(result))