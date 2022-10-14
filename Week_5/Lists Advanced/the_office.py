employee_list, happiness_improvement_factor = list(map(int,input().split())), int(input())
employee_list = [item*happiness_improvement_factor for item in employee_list]
average_happiness = sum(employee_list) / len(employee_list)


happy_list = list(filter(lambda x: x > average_happiness,employee_list))

if len(happy_list) >= len(employee_list) /2:
    print(f"Score: {len(happy_list)}/{len(employee_list)}. Employees are happy!")
else:
    print(f"Score: {len(happy_list)}/{len(employee_list)}. Employees are not happy!")