def characters_in_range(char1,char2):
    string_to_print = ''
    for number in range(ord(char1)+1,ord(char2)):
        string_to_print += chr(number) + ' '
    return string_to_print

character_1 = input()
character_2 = input()


print(characters_in_range(character_1,character_2))
