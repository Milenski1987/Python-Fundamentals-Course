students = {}
searched_course = ""

while True:
    student = input()

    if ":" not in student:
        searched_course = student
        break

    name, name_id, course = student.split(":")
    if name not in students:
        students[name] = {}
    students[name]["user_id"] = name_id
    students[name]["course"] = course

if "_" in searched_course:
    searched_course = searched_course.replace("_", " ")

for student, information in students.items():
    for course in information.values():
        if course == searched_course:
            print(f"{student} - {students[student]['user_id']}")