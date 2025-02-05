def calculate_needed_time(people_per_hour: int, people_count: int) -> int:
    hour = 0
    while True:
        if people_count <= 0:
            break

        hour += 1
        if hour % 4 == 0:
            continue
        people_count -= people_per_hour

    return hour


def main():
    first_employee_efficiency = int(input())
    second_employee_efficiency = int(input())
    third_employee_efficiency = int(input())
    students_count = int(input())
    students_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
    hours_needed = calculate_needed_time(students_per_hour, students_count)
    print(f"Time needed: {hours_needed}h.")


main()