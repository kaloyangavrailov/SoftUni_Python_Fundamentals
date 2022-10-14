number = int(input())
for letter_1 in range(number):
    for letter_2 in range(number):
        for letter_3 in range(number):
            print(f'{chr(97+letter_1)}{chr(97+letter_2)}{chr(97+letter_3)}')