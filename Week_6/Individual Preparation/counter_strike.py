battles_won = 0
initial_energy = int(input())
while True:
    distance_enemy = input()
    if distance_enemy == 'End of battle':
        print(f'Won battles: {battles_won}. Energy left: {initial_energy}')
        break
    else:
        distance_enemy = int(distance_enemy)
        if distance_enemy > initial_energy:
            print(f'Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy')
            break
        else:
            initial_energy -= distance_enemy
            battles_won += 1
            if battles_won % 3 == 0:
                initial_energy += battles_won
