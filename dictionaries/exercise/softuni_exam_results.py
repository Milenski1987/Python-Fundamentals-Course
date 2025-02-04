def create_students_data(students_data: dict, language_data: dict, current_name: str, lang: str, score: int) -> tuple:
    if lang not in language_data:
        language_data[lang] = []
    language_data[lang].append(score)
    if current_name not in students_data:
        students_data[current_name] = 0
    if score > students_data[current_name]:
        students_data[current_name] = score
    return students_data, language_data


def user_banned(students_data: dict, current_name: str) -> dict:
    if current_name in students_data:
        del students_data[current_name]
    return students_data


def main():
    students_information = {}
    language_submissions = {}

    while True:
        command = input()
        if command == "exam finished":
            break

        current_command = command.split("-")
        name = current_command[0]
        language = current_command[1]

        if language == "banned":
            students_information = user_banned(students_information, name)

        else:
            points = int(current_command[2])
            students_information, language_submissions = create_students_data(students_information,
                                                                              language_submissions, name, language,
                                                                              points)

    print("Results:")
    for student_name, student_score in students_information.items():
        print(f"{student_name} | {student_score}")
    print("Submissions:")
    for programming_language, language_submission in language_submissions.items():
        print(f"{programming_language} - {len(language_submission)}")


main()