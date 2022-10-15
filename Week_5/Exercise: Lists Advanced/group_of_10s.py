sequence_numbers_list = list(map(int,input().split(', ')))

list_total_groups = []

for group in range(10,100+1,10):
    list_groups = []
    for item in sequence_numbers_list:
        if group - 10 < item <= group:
            list_groups.append(item)
    list_total_groups.append(list_groups)

list_total_groups_copy = list_total_groups.copy()

for index in range(len(list_total_groups_copy)-1,-1,-1):
    if len(list_total_groups_copy[index]) == 0:
        list_total_groups.pop(index)
    else:
        break

for index in range(len(list_total_groups)):
    print(f"Group of {(index+1)*10}'s: {list_total_groups[index]}")
