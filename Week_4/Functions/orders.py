def product_price_calculator(product,quantity):
    if product == 'coffee': return f'{quantity*1.5:.2f}'
    elif product == 'coke': return f'{quantity*1.4:.2f}'
    elif product == 'water': return f'{quantity*1.0:.2f}'
    elif product == 'snacks': return f'{quantity*2.0:.2f}'


product = input()
quantity = int(input())

print(product_price_calculator(product,quantity))