n_numbers = int(input())

for i in range(1, n_numbers+1):
    n = int(input())
    if n % 2 != 0:
        print(f'{n} is odd!')
        break
else:
    print(f'All numbers are even.')