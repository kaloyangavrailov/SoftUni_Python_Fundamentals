number = int(input())

for digit in range(1,number+1):
    digit = str(digit)
    if len(digit) > 1:
        sum_ = int(digit[0]) + int(digit[1])
        if sum_ == 5 or sum_ == 7 or sum_ == 11:
            print(f'{digit} -> True')
        else:
            print(f'{digit} -> False')
    else:
        if digit == '5' or digit == '7' or digit == '11':
            print(f'{digit} -> True')
        else:
            print(f'{digit} -> False')
