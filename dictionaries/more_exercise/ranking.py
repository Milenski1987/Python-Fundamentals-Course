def create_contests_data(contests: dict, information_for_key: str, information_for_value: str) -> dict:
    if information_for_key not in contests:
        contests[information_for_key] = ""
    contests[information_for_key] = information_for_value
    return contests


def create_submissions_data(submissions: dict, current_contest: str, user: str, score: int) -> dict:
    if user not in submissions:
        submissions[user] = {}
    if current_contest not in submissions[user]:
        submissions[user][current_contest] = score
    if score > submissions[user][current_contest]:
        submissions[user][current_contest] = score
    return submissions


def validate_contest(contests: dict, submissions: dict, current_contest: str, password: str, user: str, score: int) -> dict:
    if current_contest in contests:
        if contests[current_contest] == password:
            submissions = create_submissions_data(submissions, current_contest, user, score)
    return submissions


def find_best_user(submissions: dict, best_name: str, best_points: int) -> tuple:
    for user, courses in submissions.items():
        current_points = 0
        for course, points in courses.items():
            current_points += points
        if current_points > best_points:
            best_points = current_points
            best_name = user
    return best_name, best_points


def main():
    submissions_data = {}
    contests_data = {}
    best_user = ""
    best_score = 0

    while True:
        command = input()
        if command == "end of contests":
            break
        contest, contest_password = command.split(":")

        contests_data = create_contests_data(contests_data, contest, contest_password)

    while True:
        command = input()
        if command == "end of submissions":
            break

        contest, contest_password, username, points = command.split("=>")
        points = int(points)
        submissions_data = validate_contest(contests_data, submissions_data, contest, contest_password, username, points)

    best_user, best_score = find_best_user(submissions_data, best_user, best_score)

    print(f"Best candidate is {best_user} with total {best_score} points.")

    submissions_data = dict(sorted(submissions_data.items()))
    print("Ranking:")
    for name, information in submissions_data.items():
        print(f"{name}")
        information = dict(sorted(information.items(), key=lambda info: -info[1]))
        for course, score in information.items():
            print(f"#  {course} -> {score}")


main()
