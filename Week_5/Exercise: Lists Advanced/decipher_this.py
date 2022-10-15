secret_message = input().split()

numbers_list = []
characters_list = []
for item in secret_message:
    number = []
    characters = []
    for char in item:
        if char.isdigit():
            number.append(char)
        elif char.isalpha():
            characters.append(char)
    numbers_list.append(number)
    characters_list.append(characters)

numbers_list = [chr(int(''.join(item))) for item in numbers_list]


for item in characters_list:
    if len(item) > 3:
        item[0],item[-1] = item[-1],item[0]
    elif len(item) == 3:
        item[0], item[2] = item[2], item[0]
    elif len(item) == 2:
        item[0], item[1] = item[1], item[0]



characters_list = [''.join(item) for item in characters_list]

final_words_list = []

for index in range(len(characters_list)):
    final_words_list.append(numbers_list[index]+characters_list[index])

print(' '.join(final_words_list))