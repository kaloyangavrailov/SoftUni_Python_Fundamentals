list_of_sequence_of_numbers = input().split()
message = input()


list_of_message = []

for letter in message:
    list_of_message.append(letter)


list_of_indexes = []
number = 0

for item in list_of_sequence_of_numbers:
    for letter in item:
        number += int(letter)
    list_of_indexes.append(number)
    number = 0


final_message = ''

for item in list_of_indexes:
    if item <= len(list_of_message):
        final_message += list_of_message[item]
        list_of_message.remove(list_of_message[item])
    else:
        corrected_index = item - len(list_of_message)
        final_message += list_of_message[corrected_index]
        list_of_message.remove(list_of_message[corrected_index])

print(final_message)
