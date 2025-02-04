def create_judge_data(judge: dict, students: dict, user: str, current_contest: str, score: int) -> tuple:
    if current_contest not in judge:
        judge[current_contest] = {}
    if user not in judge[current_contest]:
        judge[current_contest][user] = score
    if user not in students:
        students[user] = 0
    if score > judge[current_contest][user]:
        judge[current_contest][user] = score

    return judge, students

def update_individual_data(judge: dict, students: dict) -> dict:
    for course, submissions in judge.items():
        for user, score in submissions.items():
            students[user] += score
    return students

def main():
    judge_data = {}
    students_data = {}

    while True:
        command = input()

        if command == "no more time":
            break

        username, contest, points = command.split(" -> ")
        points = int(points)
        judge_data, students_data = create_judge_data(judge_data, students_data, username, contest, points)


    for contest, results in judge_data.items():
        place = 1
        print(f"{contest}: {len(results)} participants")
        results = dict(sorted(results.items(), key= lambda score: (-score[1], score[0])))
        for user, score in results.items():
            print(f"{place}. {user} <::> {score}")
            place += 1
    print("Individual standings:")
    students_data = update_individual_data(judge_data, students_data)
    students_data = dict(sorted(students_data.items(), key=lambda result: (-result[1], result[0])))
    current_place = 1
    for student, result in students_data.items():
        print(f"{current_place}. {student} -> {result}")
        current_place += 1

main()