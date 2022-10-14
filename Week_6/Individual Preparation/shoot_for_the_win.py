targets_sequence = input().split()
targets_sequence = [int(item) for item in targets_sequence]
targets_shot = 0
while True:
    index_of_target = input()
    if index_of_target == 'End':
        break
    else:
        index_of_target = int(index_of_target)
        if len(targets_sequence)-1 < index_of_target:
            continue
        else:
            value_of_target_index = targets_sequence[index_of_target]
            targets_sequence[index_of_target] = -1
            targets_shot += 1
            for index in range(len(targets_sequence)):
                if targets_sequence[index] == -1:
                    continue
                else:
                    if targets_sequence[index] <= value_of_target_index:
                        targets_sequence[index] += value_of_target_index
                    else:
                        targets_sequence[index] -= value_of_target_index

targets_sequence = [str(item) for item in targets_sequence]
print(f"Shot targets: {targets_shot} -> {' '.join(targets_sequence)}")