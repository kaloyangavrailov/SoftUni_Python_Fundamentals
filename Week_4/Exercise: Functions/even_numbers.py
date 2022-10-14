def even_number(item):
        if item % 2 == 0:
            return True

list_of_string_of_numbers = input().split()
list_of_string_of_numbers = [int(item) for item in list_of_string_of_numbers]

list_of_even_numbers = list(filter(even_number,list_of_string_of_numbers))

print(list_of_even_numbers)