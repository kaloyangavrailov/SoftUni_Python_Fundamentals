list_of_integers = input().split()
list_of_integers = [int(item) for item in list_of_integers]

loop_flag = True
while True:
    command = input()
    if command == 'end':
        break
    else:
        command_list_of_indexes = command.split()
        command = command_list_of_indexes[0]
        command_list_of_indexes.remove(command)
        command_list_of_indexes = [int(item) for item in command_list_of_indexes]

        if len(command_list_of_indexes) == 0:
            list_of_integers = [item - 1 for item in list_of_integers]
        elif len(command_list_of_indexes) == 2:
            if command == 'swap':
                list_of_integers[command_list_of_indexes[0]], list_of_integers[command_list_of_indexes[1]] = list_of_integers[command_list_of_indexes[1]], list_of_integers[command_list_of_indexes[0]]
            elif command == 'multiply':
                list_of_integers[command_list_of_indexes[0]] = list_of_integers[command_list_of_indexes[0]] * list_of_integers[command_list_of_indexes[1]]

list_of_integers = [str(item) for item in list_of_integers]

print(', '.join(list_of_integers))