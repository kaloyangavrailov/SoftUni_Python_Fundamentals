number = float(input())

if number == 0:
    print(f'zero')
elif number > 0:
    if abs(number) < 1 and abs(number) != 0:
        print(f'small positive')
    elif abs(number) > 1000000:
        print(f'large positive')
else:
    if abs(number) < 1 and abs(number) != 0:
        print(f'small negative')
    elif abs(number) > 1000000:
        print(f'large negative')