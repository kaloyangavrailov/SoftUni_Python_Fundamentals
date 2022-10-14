def sum_numbers(num1, num2):
    return num1 + num2


def subtract(sum_num1_num2, num3):
    return sum_num1_num2 - num3


def add_and_subtract(num1,num2,num3):

    result = sum_numbers(num1,num2)

    return subtract(result,num3)

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

final_print = add_and_subtract(number_1,number_2,number_3)

print(final_print)