budget = float(input())
flower_price = float(input())
eggs_price = flower_price * 0.75
liter_milk_price = flower_price * 1.25
colored_eggs = 0
loaf = 0
while True:
    if budget >= eggs_price + flower_price + liter_milk_price / 4:
        budget -= (eggs_price + flower_price + liter_milk_price / 4)
        loaf += 1
        colored_eggs += 3
        if loaf % 3 == 0:
            colored_eggs -= loaf - 2
    else:
        break
print(f'You made {loaf} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')