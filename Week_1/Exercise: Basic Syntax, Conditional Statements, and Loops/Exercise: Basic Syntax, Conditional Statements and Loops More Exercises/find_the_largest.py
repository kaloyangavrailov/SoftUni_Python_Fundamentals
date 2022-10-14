number = input()

list_number = [int(digit) for digit in number]
list_highest_number = []

while len(list_number) != 0:

    for _ in list_number:
        item_to_remove = max(list_number)
        list_number.remove(item_to_remove)
        list_highest_number.append(item_to_remove)

list_highest_number = [str(item) for item in list_highest_number]
highest_number = ''.join(list_highest_number)
print(highest_number)