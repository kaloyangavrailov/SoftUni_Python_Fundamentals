number = int(input())

for _ in range(number):
    string_ = input()

    if ',' in string_ or '.' in string_ or '_' in string_:
        print(f'{string_} is not pure!')
    else:
        print(f'{string_} is pure.')