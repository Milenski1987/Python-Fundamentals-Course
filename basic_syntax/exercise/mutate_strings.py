first_string = input()
second_string = input()

new_string = ""
last_printed_string = first_string

for index in range(len(first_string)):
    new_string = second_string[:index + 1] + first_string[index + 1:]

    if new_string != last_printed_string:
        last_printed_string = new_string
        print(new_string)