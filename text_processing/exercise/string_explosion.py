def string_explosion(current_string: str) -> str:
    result_string = ""
    explosions_left = 0
    for index in range(len(current_string)):
        if current_string[index] == ">":
            result_string += current_string[index]
            explosions_left += int(current_string[index + 1])
        else:
            if explosions_left == 0:
                result_string += current_string[index]
            else:
                explosions_left -= 1
    return result_string

def main():
    some_string = input()

    final_string = string_explosion(some_string)
    print(final_string)


main()