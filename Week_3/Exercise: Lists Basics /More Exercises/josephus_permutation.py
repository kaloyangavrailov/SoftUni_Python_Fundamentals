list_of_people = input().split()
execution_index = int(input())
list_people_executed = []
start_index = execution_index - 1
list_of_people_copy = list_of_people.copy()

total_list_of_people = list_of_people + list_of_people_copy

print(total_list_of_people)

for person in (start_index,len(total_list_of_people),execution_index):
    list_people_executed.append(total_list_of_people[person])
    for person_x in total_list_of_people:
        if person_x == total_list_of_people[person]:
            total_list_of_people.remove(person_x)
