def valid_password(password):
    pass_valid = True
    message_1 = ''
    message_2 = ''
    message_3 = ''
    count = 0
    if 6 > len(password) or len(password) > 10:
        message_1 = "Password must be between 6 and 10 characters"
        pass_valid = False
    if not password.isalnum():
        message_2 = "Password must consist only of letters and digits"
        pass_valid = False
    for character in password:

        if character.isdigit():
              count += 1
        else:
            continue
    if count < 2:
        message_3 = "Password must have at least 2 digits"
        pass_valid = False
    return message_1,message_2,message_3, pass_valid

pass_word = input()
first_message, second_message, third_message, password_valid_flag = valid_password(pass_word)

if password_valid_flag:
    print(f'Password is valid')
else:
    if first_message == '':
        print(f'{second_message}\n{third_message}')
    elif first_message == '' and second_message == '':
        print(f'{third_message}')
    elif third_message == '':
        print(f'{first_message}\n{second_message}')
    elif second_message == '':
        print(f'{first_message}\n{third_message}')
    elif second_message == '' and third_message == '':
        print(f'{first_message}')
    else:
        print(f'{first_message}\n{second_message}\n{third_message}')