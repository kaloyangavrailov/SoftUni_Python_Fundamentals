number_of_snowballs = int(input())
highest_value = 0
for snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    time_needed = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / time_needed) ** snowball_quality
    if snowball_value > highest_value:
        highest_value = snowball_value
        highest_value_snowball_weight = snowball_weight
        highest_value_snowball_time = time_needed
        highest_value_snowball_quality = snowball_quality
print(f'{highest_value_snowball_weight} : {highest_value_snowball_time} = {int(highest_value)} ({highest_value_snowball_quality})')