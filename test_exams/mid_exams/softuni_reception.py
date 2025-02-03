def time_needed(students_per_hour: int, total_students: int) -> int:
    time = 0
    while total_students > 0:
        time += 1
        if time % 4 == 0:
            continue
        total_students -= students_per_hour
    return time


def main():
    first_employee_efficiency = int(input())
    second_employee_efficiency = int(input())
    third_employee_efficiency = int(input())
    students_count = int(input())

    students_handled_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
    result = time_needed(students_handled_per_hour, students_count)

    print(f"Time needed: {result}h.")


main()

