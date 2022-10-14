def get_factorial(num):
    for digit in range(1,num):
        num *= digit
    return num

number_1 = int(input())
number_2 = int(input())

factorial_number_1 = get_factorial(number_1)
factorial_number_2 = get_factorial(number_2)

print(f'{factorial_number_1/factorial_number_2:.2f}')
