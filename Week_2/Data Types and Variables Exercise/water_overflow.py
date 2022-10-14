capacity = 255
number_of_lines = int(input())
liters_in_tank = 0
for _ in range(number_of_lines):
    liters_of_water = int(input())
    if capacity < 0 or capacity < liters_of_water:
        print(f"Insufficient capacity!")
    else:
        capacity -= liters_of_water
        liters_in_tank += liters_of_water
print(liters_in_tank)