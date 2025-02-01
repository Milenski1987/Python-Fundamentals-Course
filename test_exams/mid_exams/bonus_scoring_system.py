from math import ceil


def check_student_bonus(best_bonus: int, best_attendances: int, lectures: int, bonus: int) -> tuple:
    student_attendances = int(input())

    total_bonus = student_attendances / lectures * (5 + bonus)

    if total_bonus > best_bonus:
        best_bonus = total_bonus
        best_attendances = student_attendances

    return best_bonus, best_attendances


def main():
    number_of_students = int(input())
    number_of_lectures = int(input())
    additional_bonus = int(input())

    max_bonus = 0
    max_attendances = 0
    bonus_formula =number_of_lectures * (5 + additional_bonus)

    for _ in range(number_of_students):
        max_bonus, max_attendances = check_student_bonus(max_bonus, max_attendances, number_of_lectures, additional_bonus)

    print(f"Max Bonus: {ceil(max_bonus)}.\nThe student has attended {max_attendances} lectures.")


main()