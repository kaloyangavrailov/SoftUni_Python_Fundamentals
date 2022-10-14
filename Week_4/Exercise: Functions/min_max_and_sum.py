list_integers = input().split()
list_integers = [int(item) for item in list_integers]

min_number = min(list_integers)
max_number = max(list_integers)
sum_number = sum(list_integers)

print(f'The minimum number is {min_number}')
print(f'The maximum number is {max_number}')
print(f'The sum number is: {sum_number}')
