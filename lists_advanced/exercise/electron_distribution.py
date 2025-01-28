number_of_electrons = int(input())
shells = []
shell_position = 1

while number_of_electrons > 0:
    max_electrons_on_that_shell = 2 * shell_position ** 2

    if number_of_electrons > max_electrons_on_that_shell:
        shells.append(max_electrons_on_that_shell)
        number_of_electrons -= max_electrons_on_that_shell
    else:
        shells.append(number_of_electrons)
        number_of_electrons = 0

    shell_position += 1

print(shells)