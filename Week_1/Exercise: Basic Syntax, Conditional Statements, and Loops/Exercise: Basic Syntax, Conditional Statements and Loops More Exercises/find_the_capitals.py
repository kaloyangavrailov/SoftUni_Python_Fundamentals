string_ = input()
list_letters = []
for letter in range(len(string_)):
    if 65 <= ord(string_[letter]) <= 90:
        list_letters.append(letter)

print(list_letters)