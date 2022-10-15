def function_add(lesson,list_courses):
    if lesson not in list_courses:
        list_courses.append(lesson)
    return list_courses


def function_insert(lesson,index,list_courses):
    if lesson not in list_courses:
        list_courses.insert(int(index),lesson)
    return list_courses


def function_remove(lesson,list_courses):
    if lesson in list_courses:
        list_courses.remove(lesson)
    return list_courses


def function_swap(lesson_1,lesson_2,list_courses):
    if lesson_1 in list_courses and lesson_2 in list_courses:
        index_lesson_1 = list_courses.index(lesson_1)
        index_lesson_2 = list_courses.index(lesson_2)
        if index_lesson_2 == len(list_courses)-1:
            if 'Exercise' in list_courses[index_lesson_1 + 1]:
                list_courses[index_lesson_1], list_courses[index_lesson_2] \
                    = list_courses[index_lesson_2], list_courses[index_lesson_1]
                exercise = list_courses.pop(index_lesson_1 + 1)
                list_courses.append(exercise)
            else:
                list_courses[index_lesson_1], list_courses[index_lesson_2] \
                    = list_courses[index_lesson_2], list_courses[index_lesson_1]
        else:
            if 'Exercise' in list_courses[index_lesson_1+1] and 'Exercise' not in list_courses[index_lesson_2+1]:
                list_courses[index_lesson_1], list_courses[index_lesson_2] \
                    = list_courses[index_lesson_2], list_courses[index_lesson_1]
                exercise = list_courses.pop(index_lesson_1+1)
                list_courses.insert(index_lesson_2+1,exercise)
            elif 'Exercise' in list_courses[index_lesson_2+1] and 'Exercise' not in list_courses[index_lesson_1+1]:
                list_courses[index_lesson_1], list_courses[index_lesson_2] \
                    = list_courses[index_lesson_2], list_courses[index_lesson_1]
                exercise = list_courses.pop(index_lesson_2+1)
                list_courses.insert(index_lesson_1+1,exercise)
            elif 'Exercise' not in list_courses[index_lesson_1+1] and 'Exercise' not in list_courses[index_lesson_2+1]:
                list_courses[index_lesson_1], list_courses[index_lesson_2] \
                    = list_courses[index_lesson_2], list_courses[index_lesson_1]
            elif 'Exercise' in list_courses[index_lesson_1+1] and 'Exercise' in list_courses[index_lesson_2+1]:
                list_courses[index_lesson_1], list_courses[index_lesson_2] \
                    = list_courses[index_lesson_2], list_courses[index_lesson_1]
                exercise_1 = list_courses.pop(index_lesson_1+1)
                exercise_2 = list_courses.pop(index_lesson_2+1)
                list_courses.insert(index_lesson_2+1,exercise_1)
                list_courses.insert(index_lesson_1 + 1, exercise_2)
    return list_courses


def function_exercise(lesson,list_courses):
    if lesson in list_courses:
        exercise_index = list_courses.index(lesson) + 1
        if 'Exercise' in list_courses[exercise_index]:
            return list_courses
        elif 'Exercise' not in list_courses[exercise_index]:
            list_courses.insert(exercise_index,f'{lesson}-Exercise')
    else:
        list_courses.append(lesson)
        list_courses.append(f'{lesson}-Exercise')
    return list_courses


list_courses = input().split(', ')


while True:
    command = input()
    if command == 'course start':
        break
    else:
        command = command.split(':')
        if command[0] == 'Add' or command[0] == 'Remove' or command[0] == 'Exercise':
            lesson_title = command[1]
            if command[0] == 'Add':
                list_courses = function_add(lesson_title,list_courses)
            elif command[0] == 'Remove':
                list_courses = function_remove(lesson_title,list_courses)
            elif command[0] == 'Exercise':
                list_courses = function_exercise(lesson_title,list_courses)
        elif command[0] == 'Insert' or command[0] == 'Swap':
            lesson_title = command[1]
            lessen_title_2_or_index = command[2]
            if command[0] == 'Insert':
                list_courses = function_insert(lesson_title,lessen_title_2_or_index,list_courses)
            elif command[0] == 'Swap':
                list_courses = function_swap(lesson_title,lessen_title_2_or_index,list_courses)

[print(f'{item+1}.{list_courses[item]}') for item in range(len(list_courses))]
