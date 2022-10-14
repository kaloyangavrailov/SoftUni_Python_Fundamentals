
transformed_string = ''
while True:
    string_ = input()
    if string_ == 'End':
        break
    if string_ == 'SoftUni':
        continue
    for char in string_:
        transformed_string += char*2
    print(transformed_string)
    transformed_string = ''