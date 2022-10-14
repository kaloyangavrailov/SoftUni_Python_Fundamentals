number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
list_students_attendances = []

for student in range(number_of_students):
    student_attendances = int(input())
    list_students_attendances.append(student_attendances)

highest_attendance_score = max(list_students_attendances)

total_bonus = highest_attendance_score / number_of_lectures * (5 + additional_bonus)

print(f"""
Max Bonus: {round(total_bonus)}.
The student has attended {highest_attendance_score} lectures.
""")