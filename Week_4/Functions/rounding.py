def number_rounding(list_numbers):
    list_numbers = [round(item) for item in list_numbers]
    return list_numbers

list_numbers = input().split()

list_numbers = [float(item) for item in list_numbers]

list_numbers = number_rounding(list_numbers)

print(list_numbers)