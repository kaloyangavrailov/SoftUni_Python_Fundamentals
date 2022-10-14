initial_list_groceries = input().split('!')
loop_flag = True
while loop_flag:
    command = input()
    if command == 'Go Shopping!':
        loop_flag = False
    else:
        list_command = command.split()
        if len(list_command) == 2:
            key_word = list_command[0]
            item = list_command[1]
            if key_word == 'Urgent':
                if item in initial_list_groceries:
                    continue
                else:
                    initial_list_groceries.insert(0,item)
            elif key_word == 'Unnecessary':
                if item not in initial_list_groceries:
                    continue
                else:
                    initial_list_groceries.remove(item)
            elif key_word == 'Rearrange':
                if item not in initial_list_groceries:
                    continue
                else:
                    initial_list_groceries.remove(item)
                    initial_list_groceries.append(item)
        elif len(list_command) == 3:
            key_word = list_command[0]
            old_item = list_command[1]
            new_item = list_command[2]
            if old_item not in initial_list_groceries:
                continue
            else:
                index = initial_list_groceries.index(old_item)
                initial_list_groceries[index] = new_item
print(', '.join(initial_list_groceries))