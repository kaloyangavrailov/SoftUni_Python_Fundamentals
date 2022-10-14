fires_with_their_cells_list = input().split('#')
water_available = int(input())
effort = 0
list_of_cells = []
total_fire = 0
for item in fires_with_their_cells_list:
    fire_type, cell_value = item.split(' = ')
    cell_value = int(cell_value)
    if water_available < cell_value:
        continue
    else:
        if (81 <= cell_value <= 125 and fire_type == 'High') \
                or (51 <= cell_value <= 80 and fire_type == 'Medium')\
                or (1 <= cell_value <= 50 and fire_type == 'Low'):
            list_of_cells.append(' - '+str(cell_value))
            water_available -= cell_value
            effort += cell_value * 0.25
            total_fire += cell_value
        else:
            continue
print('Cells:')
for item in list_of_cells:
    print(item)
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')