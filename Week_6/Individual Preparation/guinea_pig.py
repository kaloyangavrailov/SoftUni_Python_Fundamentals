quantity_food_kg = float(input())
quantity_hay_kilograms = float(input())
quantity_cover_kilograms = float(input())
pig_wight_kilograms = float(input())
day_counter = 0

while day_counter < 30:
    quantity_food_kg = round(quantity_food_kg,2)
    day_counter += 1
    if quantity_hay_kilograms <= 0 or quantity_cover_kilograms <= 0 or quantity_cover_kilograms <= 0:
        break
    else:
        if day_counter % 3 == 0:
            quantity_cover_kilograms -= pig_wight_kilograms / 3
        if day_counter % 2 == 0:
            quantity_food_kg -= 0.3
            quantity_hay_kilograms -= quantity_food_kg * 0.05
        else:
            quantity_food_kg -= 0.3


if quantity_hay_kilograms <= 0.0 or quantity_food_kg <= 0.0 or quantity_cover_kilograms <= 0.0:
    print(f'Merry must go to the pet store!')
else:
    print(f'Everything is fine! Puppy is happy! Food: {quantity_food_kg:.2f}, Hay: {quantity_hay_kilograms:.2f}, Cover: {quantity_cover_kilograms:.2f}.')