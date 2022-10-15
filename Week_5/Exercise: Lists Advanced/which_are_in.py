list_substrings = input().split(', ')
list_strings = input().split(', ')
list_matches = []

for substring in list_substrings:
    for string in list_strings:
        if substring in string:
            list_matches.append(substring)
            break
print(list_matches)