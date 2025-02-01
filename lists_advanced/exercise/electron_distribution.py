def electron_distribution(shell_status: list,max_electrons_for_shell: int, electrons_count: int) -> tuple:
    if electrons_count > max_electrons_for_shell:
        shell_status.append(max_electrons_for_shell)
        electrons_count -= max_electrons_for_shell
    else:
        shell_status.append(electrons_count)
        electrons_count = 0

    return shell_status, electrons_count


number_of_electrons = int(input())
shells = []
shell_position = 1

while number_of_electrons > 0:
    max_electrons_on_that_shell = 2 * shell_position ** 2
    shells, number_of_electrons = electron_distribution(shells, max_electrons_on_that_shell, number_of_electrons)
    shell_position += 1

print(shells)