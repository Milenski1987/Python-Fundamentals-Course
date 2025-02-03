def register_courses_and_students(courses_data: dict, course: str, name: str) -> dict:
    if course not in courses_data:
        courses_data[course] = []
    courses_data[course].append(name)
    return courses_data


def print_information(courses_data: dict):
    for course, students in courses_data.items():
        print(f"{course}: {len(courses_data[course])}")
        for name in students:
            print(f"-- {name}")

def main():
    courses = {}

    while True:
        command = input()

        if command == "end":
            print_information(courses)
            break

        course_information = command.split(" : ")
        current_course = course_information[0]
        student_name = course_information[1]

        register_courses_and_students(courses, current_course, student_name)


main()

