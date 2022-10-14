def perfect_or_not(num):
    aliquot_sum = 0
    for digit in range(1,(num//2)+1):
        if num%digit == 0:
            aliquot_sum += digit
    if aliquot_sum == num:
        return f'We have a perfect number!'
    else:
        return f"It's not so perfect."

number = int(input())

print(perfect_or_not(number))