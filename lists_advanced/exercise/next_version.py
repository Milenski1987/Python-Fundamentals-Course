current_version = input().split(".")
next_version = list(str(int("".join(current_version)) + 1))
print(".".join(next_version))