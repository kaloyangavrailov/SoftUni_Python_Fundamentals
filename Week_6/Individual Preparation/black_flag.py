days_pirating = int(input())
daily_plunder = int(input())
expected_plunder = int(input())
plunder_gathered = 0
for day in range(1,days_pirating+1):
    if day % 3 == 0:
        plunder_gathered += daily_plunder * 1.5
    if day % 3 != 0:
        plunder_gathered += daily_plunder
    if day % 5 == 0:
        plunder_gathered -= plunder_gathered * 0.3

if plunder_gathered >= expected_plunder:
    print(f'Ahoy! {plunder_gathered:.2f} plunder gained.')
else:
    print(f'Collected only {(plunder_gathered/expected_plunder)*100:.2f}% of the plunder.')