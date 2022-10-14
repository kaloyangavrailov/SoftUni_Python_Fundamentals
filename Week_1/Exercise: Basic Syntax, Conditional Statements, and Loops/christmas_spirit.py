quantity_decorations = int(input())
days_until_xmas = int(input())

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
money_for_decorations = 0
xmas_spirit = 0
if days_until_xmas % 10 == 0:
    xmas_spirit -= 30
while days_until_xmas != 0:
    if days_until_xmas % 11 == 0:
        quantity_decorations += 2
    if days_until_xmas % 2 == 0:
        money_for_decorations += ornament_set * quantity_decorations
        xmas_spirit += 5
    if days_until_xmas % 3 == 0:
        money_for_decorations += (tree_skirt + tree_garland) * quantity_decorations
        xmas_spirit += 13
    if days_until_xmas % 5 == 0:
        if days_until_xmas % 3 == 0:
            xmas_spirit += 30
        money_for_decorations += tree_lights * quantity_decorations
        xmas_spirit += 17
    if days_until_xmas % 10 == 0:
        xmas_spirit -= 20
        money_for_decorations += 23
    days_until_xmas -= 1
print(f"""
Total cost: {money_for_decorations}
Total spirit: {xmas_spirit}
""")