def add(course, title):
    if title not in course:
        course.append(title)

def inserting(course, title, idx):
    if idx in range(len(course)):
        if title not in course:
            course.insert(idx, title)

def removing(course, title):
    lesson_exercise = f"{title}-Exercise"
    if title in course:
        course.remove(title)
        if lesson_exercise in course:
            course.remove(lesson_exercise)

def swap(course, first_title, second_title):

    if first_title in course and second_title in course:
        first_title_index = course.index(first_title)
        second_title_index = course.index(second_title)

        course[first_title_index], course[second_title_index] = course[second_title_index], course[first_title_index]

    first_lesson_exercise = f"{first_title}-Exercise"
    second_lesson_exercise = f"{second_title}-Exercise"

    if first_lesson_exercise in course:
        first_exercise_index = course.index(first_lesson_exercise)
        exercise_to_swap = course.pop(first_exercise_index)
        course.insert(second_title_index + 1, exercise_to_swap)


    if second_lesson_exercise in course:
        second_exercise_index = course.index(second_lesson_exercise)
        exercise_to_swap = course.pop(second_exercise_index)
        course.insert(first_title_index + 1, exercise_to_swap)



def exercise(course, title):
    lesson_exercise = f"{title}-Exercise"
    if lesson_exercise not in course:
        if title not in course:
            course.append(title)
            course.append(lesson_exercise)
        else:
            title_index = course.index(title)
            course.insert(title_index + 1, lesson_exercise)

initial_course = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break

    current_command = command.split(":")
    action = current_command[0]
    lesson_title = current_command[1]


    if action == "Add":
        add(initial_course, lesson_title)

    elif action == "Insert":
        index = int(current_command[2])
        inserting(initial_course, lesson_title, index)

    elif action == "Remove":
        removing(initial_course, lesson_title)

    elif action == "Swap":
        other_title = current_command[2]
        swap(initial_course, lesson_title, other_title)

    elif action == "Exercise":
        exercise(initial_course, lesson_title)

for index, value in enumerate(initial_course):
    print(f"{index + 1}.{value}")