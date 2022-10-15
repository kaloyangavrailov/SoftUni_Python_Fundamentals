def index_manipulator_function(position_of_pokemon,list_of_pokemons):
    if position_of_pokemon < 0:
        captured_pokemon = list_of_pokemons[0]
        list_of_pokemons[0] = list_of_pokemons[-1]
        list_of_pokemons = increase_decrease_function(list_of_pokemons,captured_pokemon)
    elif position_of_pokemon > len(list_of_pokemons)-1:
        captured_pokemon = list_of_pokemons[-1]
        list_of_pokemons[-1] = list_of_pokemons[0]
        list_of_pokemons = increase_decrease_function(list_of_pokemons,captured_pokemon)
    else:
        captured_pokemon = list_of_pokemons.pop(position_of_pokemon)
        list_of_pokemons = increase_decrease_function(list_of_pokemons,captured_pokemon)
    return list_of_pokemons, captured_pokemon


def increase_decrease_function(list_pokemons,captured_pokemon):
    list_pokemons = [item + captured_pokemon if item <= captured_pokemon else item - captured_pokemon for item in
                        list_pokemons]
    return list_pokemons


sequence_of_integers = list(map(int,input().split()))

sum_removed_elements = 0

while sequence_of_integers:
    integer_index = int(input())
    sequence_of_integers, removed_element = index_manipulator_function(integer_index,sequence_of_integers)
    sum_removed_elements += removed_element

print(sum_removed_elements)