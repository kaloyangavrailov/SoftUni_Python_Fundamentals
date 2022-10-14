list_of_given_numbers = input().split()
amount_to_remove = int(input())

list_of_given_numbers = [int(item) for item in list_of_given_numbers]


for iteration in range(amount_to_remove):
    list_of_given_numbers.remove(min(list_of_given_numbers))

list_of_given_numbers = [str(item) for item in list_of_given_numbers]
string_of_list_of_given_numbers = ', '.join(list_of_given_numbers)

print(string_of_list_of_given_numbers)