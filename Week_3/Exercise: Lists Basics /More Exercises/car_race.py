race_track_list = input().split()

race_track_list = [int(item) for item in race_track_list]

total_time_driver_a = 0
total_time_driver_b = 0
count_a = 0
count_b = 0
for item in race_track_list:
    if count_a == (len(race_track_list) - 1) / 2:
        break
    else:
        count_a += 1
        if item == 0:
            total_time_driver_a = total_time_driver_a * 0.8
        else:
            total_time_driver_a += item

for item in reversed(race_track_list):
    if count_b == (len(race_track_list) - 1) / 2:
        break
    else:
        count_b += 1
        if item == 0:
            total_time_driver_b = total_time_driver_b * 0.8
        else:
            total_time_driver_b += item

if total_time_driver_a < total_time_driver_b:
    print(f"The winner is left with total time: {total_time_driver_a:.1f}")
else:
    print(f'The winner is right with total time: {total_time_driver_b:.1f}')