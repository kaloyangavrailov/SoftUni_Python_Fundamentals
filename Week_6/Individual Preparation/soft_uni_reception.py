students_per_hour_employee_1 = int(input())
students_per_hour_employee_2 = int(input())
students_per_hour_employee_3 = int(input())
students_count = int(input())
answered_students = 0
total_efficiency = students_per_hour_employee_1 + students_per_hour_employee_2 + students_per_hour_employee_3
counter = 0
while students_count>0:
    if total_efficiency / students_count == 0:
        print(f"Time needed: {total_efficiency / students_count}h.")
    else:
        counter += 1
        if counter % 4 == 0:
            continue
        answered_students += total_efficiency
        students_count -= total_efficiency
print(f'Time needed: {counter}h.')
