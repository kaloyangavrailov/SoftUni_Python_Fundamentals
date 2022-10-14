list_ = input().split(', ')

sheep_counter = len(list_)
if list_[-1] == 'wolf':
    print(f'Please go away and stop eating my sheep')
else:
    wolf_index = list_.index('wolf') + 1
    print(f'Oi! Sheep number {sheep_counter-wolf_index}! You are about to be eaten by a wolf!')
