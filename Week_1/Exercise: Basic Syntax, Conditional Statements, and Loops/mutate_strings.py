string_1 = input()
string_2 = input()
last_string_printed = string_1

for i in range(len(string_1)):

    if last_string_printed != string_2[:i:]+string_1[i::]:
        print(f'{string_2[:i:]}{string_1[i::]}')
        last_string_printed = string_2[:i:]+string_1[i::]
