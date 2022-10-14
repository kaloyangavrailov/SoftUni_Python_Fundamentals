people_waiting_to_get_on = int(input())

wagons_ot_lift = input().split()

wagons_ot_lift = [int(wagon) for wagon in wagons_ot_lift]
counter = 0
while True:
    for wagon_index in range(len(wagons_ot_lift)):
        if wagons_ot_lift[wagon_index] == 4:
            continue
        else:
            for seat in range(wagons_ot_lift[wagon_index],4,1):
                if people_waiting_to_get_on == 0:
                    break
                people_waiting_to_get_on -= 1
                counter += 1
            wagons_ot_lift[wagon_index] = counter + wagons_ot_lift[wagon_index]
            counter = 0

    break

if sum(wagons_ot_lift) < len(wagons_ot_lift) * 4:
    wagons_ot_lift = [str(wagon) for wagon in wagons_ot_lift]
    print(f"""The lift has empty spots!
{' '.join(wagons_ot_lift)}""")
else:
    wagons_ot_lift = [str(wagon) for wagon in wagons_ot_lift]
    print(f"""There isn't enough space! {people_waiting_to_get_on} people in a queue!
{' '.join(wagons_ot_lift)}""")