def calculator(n1,n2,oper):
    if oper == 'multiply':
        return n1 * n2
    elif oper == 'divide':
        return int(n1 / n2)
    elif oper == 'add':
        return n1 + n2
    elif oper == 'subtract':
        return n1 - n2


operator = input()
number_1 = int(input())
number_2 = int(input())
result = calculator(number_1,number_2,operator)

print(result)