electrons_to_fill = int(input())
list_of_electrons = []

for position_shell in range(1,999):
    shell = 2 * (position_shell ** 2)
    if shell < electrons_to_fill:
        list_of_electrons.append(shell)
        electrons_to_fill -= shell
    else:
        list_of_electrons.append(electrons_to_fill)
        break
print(list_of_electrons)