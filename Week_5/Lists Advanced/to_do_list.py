list_of_notes = []
while True:
    to_do_notes = input()
    if to_do_notes == 'End':
        break
    else:
        priority, note = to_do_notes.split('-')
        list_of_notes.append([priority,note])

list_of_notes.sort()
list_of_notes_sorted = [item[1] for item in list_of_notes]
print(list_of_notes_sorted)