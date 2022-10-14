gifts_planned_for_purchase = input().split()

cycle_flag = True

while cycle_flag:
    command_read = input()
    if command_read == 'No Money':
        break
    else:
        command_read = command_read.split()
    if len(command_read) == 2:
        word_combination = command_read[0]
        gift = command_read[1]
    elif len(command_read) == 3:
        word_combination = command_read[0]
        gift = command_read[1]
        list_index = command_read[2]

    if word_combination == 'OutOfStock':
        if gift in gifts_planned_for_purchase:
            for item in gifts_planned_for_purchase:
                if item == gift:
                    gifts_planned_for_purchase.remove(item)
        else:
            continue
    elif word_combination == 'Required':
        if int(list_index) <= len(gifts_planned_for_purchase):
            list_index = int(list_index) -1
            gifts_planned_for_purchase[list_index] = gift
        else:
            continue
    elif word_combination == 'JustInCase':
        gifts_planned_for_purchase[-1] = gift

gifts_planned_for_purchase = [item for item in gifts_planned_for_purchase if item != 'None']

print(' '.join(gifts_planned_for_purchase))