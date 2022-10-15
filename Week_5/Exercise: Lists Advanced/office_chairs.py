number_of_rooms = int(input())
number_of_rooms_list = []
if_statement_flag = True
for room in range(number_of_rooms):
    chairs, visitors = input().split()
    difference = len(chairs) - int(visitors)
    if difference < 0:
        if_statement_flag = False
        print(f'{abs(difference)} more chairs needed in room {room+1}')
    else:
        number_of_rooms_list.append(difference)
if if_statement_flag:
    print(f'Game On, {sum(number_of_rooms_list)} free chairs left')