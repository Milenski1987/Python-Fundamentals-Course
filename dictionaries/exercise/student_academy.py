def add_student(students_data: dict, name: str, grade: float) -> dict:
    if name not in students_data:
        students_data[name] = []
    students_data[name].append(grade)
    return students_data


def clear_low_grade_students(students_data: dict) -> dict:
    final_students_data = {}
    for student, grades in students_data.items():
        average_grade = sum(grades) / len(grades)
        if average_grade >= 4.50:
            final_students_data[student] = average_grade
    return final_students_data


def main():
    number_of_students = int(input())
    students = {}

    for _ in range(number_of_students):
        student_name = input()
        student_grade = float(input())
        students = add_student(students, student_name, student_grade)

    students = clear_low_grade_students(students)

    if students:
        for student, grades in students.items():
            print(f"{student} -> {grades:.2f}")


main()