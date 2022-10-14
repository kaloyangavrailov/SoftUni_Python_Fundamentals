needed_coffees = 0
while True:
    command = input()

    if command == 'END':
        break

    if command.lower() == 'coding' or command.lower() == 'dog' \
            or command.lower() == 'cat' or command.lower() == 'movie':
        if command.islower():
            needed_coffees += 1
        else:
            needed_coffees += 2
    else:
        continue
if needed_coffees > 5:
    print(f'You need extra sleep')
else:
    print(f'{needed_coffees}')