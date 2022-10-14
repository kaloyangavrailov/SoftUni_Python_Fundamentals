budget = int(input())
purchase = input()
while True:
    if purchase == 'End':
        print(f'You bought everything needed.')
        break
    purchase = int(purchase)
    budget -= purchase
    if budget < 0:
        print(f'You went in overdraft!')
        break
    purchase = input()
