initial_health = 100
bitcoins = 0
room_counter = 0
list_dungeon_rooms = input().split('|')
died_flag = False
health_not_needed  = 0
for room in list_dungeon_rooms:
    encounter, value = room.split()
    room_counter += 1
    if encounter != 'chest' and encounter != 'potion':
        initial_health -= int(value)
        if initial_health <= 0:
            died_flag = True
            print(f"You died! Killed by {encounter}.")
            print(f"Best room: {room_counter}")
            break
        else:
            print(f"You slayed {encounter}.")
    else:
        if encounter == 'chest':
            bitcoins += int(value)
            print(f"You found {value} bitcoins.")
        elif encounter == 'potion':
            initial_health += int(value)
            if initial_health > 100:
                health_not_needed = initial_health - 100
                initial_health = 100
            print(f"You healed for {int(value)-health_not_needed} hp.")
            print(f"Current health: {initial_health} hp.")
            health_not_needed = 0


if not died_flag:
    print(f"""You've made it!
Bitcoins: {bitcoins}
Health: {initial_health}
    """)
