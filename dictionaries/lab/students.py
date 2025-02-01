def create_students_data(students_data: dict, current_name: str, current_id: str, current_course: str) -> dict:
    if current_name not in students_data:
        students_data[current_name] = {}
    students_data[current_name]["user_id"] = current_id
    students_data[current_name]["course"] = current_course
    return students_data


def search_for_student(students_data: dict,current_student: str, current_information: dict, current_course_to_search: str) -> str:
    for course in current_information.values():
        if course == current_course_to_search:
            return f"{current_student} - {students_data[current_student]['user_id']}"


def main():
    students = {}
    searched_course = ""

    while True:
        student = input()
        if ":" not in student:
            searched_course = student
            break
        name, name_id, course = student.split(":")

        students = create_students_data(students, name, name_id, course)


    if "_" in searched_course:
        searched_course = searched_course.replace("_", " ")

    for student, information in students.items():
        result = search_for_student(students, student, information, searched_course)
        if result:
            print(result)


main()