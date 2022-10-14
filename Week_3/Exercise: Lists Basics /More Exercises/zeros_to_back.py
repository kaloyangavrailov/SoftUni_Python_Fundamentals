list_of_numbers = input().split(', ')
zero = 0
list_of_numbers = [int(item) for item in list_of_numbers]

for digit in range(len(list_of_numbers)):
    if list_of_numbers[digit] == 0:
        list_of_numbers.remove(list_of_numbers[digit])
        list_of_numbers.append(zero)

print(list_of_numbers)