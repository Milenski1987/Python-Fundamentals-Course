first_employee_students_per_hour = int(input())
second_employee_students_per_hour = int(input())
third_employee_students_per_hour = int(input())

number_of_students = int(input())

total_students_per_hour = first_employee_students_per_hour + second_employee_students_per_hour + third_employee_students_per_hour
hour = 0

while True:

    if number_of_students <= 0:
        print(f"Time needed: {hour}h.")
        break

    hour += 1

    if hour % 4 == 0:
        continue

    number_of_students -= total_students_per_hour


