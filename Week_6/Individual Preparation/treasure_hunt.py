chest_of_loot_list = input().split('|')

while True:
    command = input()
    if command == 'Yohoho!':
        break
    else:
        list_command = command.split()
        if list_command[0] == 'Loot':
            for item in list_command:
                if item == 'Loot':
                    continue
                else:
                    if item in chest_of_loot_list:
                        continue
                    else:
                        chest_of_loot_list.insert(0,item)
        elif list_command[0] == 'Drop':
            if int(list_command[1]) > len(chest_of_loot_list):
                continue
            else:
                item_dropped = chest_of_loot_list.pop(int(list_command[1]))
                chest_of_loot_list.append(item_dropped)
        elif list_command[0] == 'Steal':
            list_stolen_items = []
            if int(list_command[1]) >= len(chest_of_loot_list):
                print(', '.join(chest_of_loot_list))
                chest_of_loot_list = []
            else:
                chest_of_loot_list_copy = chest_of_loot_list.copy()
                for item in range(len(chest_of_loot_list)-int(list_command[1]),len(chest_of_loot_list)):
                    item_stolen = chest_of_loot_list_copy[item]
                    list_stolen_items.append(item_stolen)
                    chest_of_loot_list.remove(item_stolen)
                print(', '.join(list_stolen_items))
if len(chest_of_loot_list) == 0:
    print(f'Failed treasure hunt.')
else:
    sum_of_values = 0
    for item in chest_of_loot_list:
        sum_of_values += len(item)
    print(f'Average treasure gain: {sum_of_values/len(chest_of_loot_list):.2f} pirate credits.')