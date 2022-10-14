number_messages_sent = int(input())

for _ in range(number_messages_sent):
    message_number = int(input())

    if message_number == 88:
        print('Hello')
    elif message_number == 86:
        print(f'How are you?')
    elif message_number < 88:
        print(f'GREAT!')
    elif message_number > 88:
        print(f'Bye.')