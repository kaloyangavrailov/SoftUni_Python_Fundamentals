customer_type = ''
total_price_parts_before_tax = 0
while True:
    part = input()
    if part == 'special' or part == 'regular':
        customer_type = part
        break
    part = float(part)
    if part < 1:
        print(f'Invalid price!')
        continue
    else:
        total_price_parts_before_tax += part
taxes = total_price_parts_before_tax * 0.2
if customer_type == 'regular':
    total_price_parts_after_tax = total_price_parts_before_tax + taxes
elif customer_type == 'special':
    total_price_parts_after_tax = (total_price_parts_before_tax + taxes) * 0.9

if total_price_parts_after_tax == 0:
    print(f'Invalid order!')
else:
    print(f"""Congratulations you've just bought a new computer!
    Price without taxes: {total_price_parts_before_tax:.2f}$
    Taxes: {taxes:.2f}$
    -----------
    Total price: {total_price_parts_after_tax:.2f}$
    """)