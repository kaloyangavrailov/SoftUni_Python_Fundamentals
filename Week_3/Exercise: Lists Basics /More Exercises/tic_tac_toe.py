line_1 = input().split()
line_2 = input().split()
line_3 = input().split()

tic_tac_toe_board = []
tic_tac_toe_board.append(line_1)
tic_tac_toe_board.append(line_2)
tic_tac_toe_board.append(line_3)

if (tic_tac_toe_board[0][0] == tic_tac_toe_board[0][1] == tic_tac_toe_board[0][2]) or \
    (tic_tac_toe_board[1][0] == tic_tac_toe_board[1][1] == tic_tac_toe_board[1][2]) or \
    (tic_tac_toe_board[2][0] == tic_tac_toe_board[2][1] == tic_tac_toe_board[2][2]) or \
    (tic_tac_toe_board[0][0] == tic_tac_toe_board[1][0] == tic_tac_toe_board[2][0]) or \
    (tic_tac_toe_board[0][1] == tic_tac_toe_board[1][1] == tic_tac_toe_board[2][1]) or \
    (tic_tac_toe_board[0][2] == tic_tac_toe_board[1][2] == tic_tac_toe_board[2][2]) or \
    (tic_tac_toe_board[0][0] == tic_tac_toe_board[1][1] == tic_tac_toe_board[2][2]) or \
    (tic_tac_toe_board[0][2] == tic_tac_toe_board[1][1] == tic_tac_toe_board[2][0]):
    if tic_tac_toe_board[1][1] == '1':
        print(f'First player won')
    elif tic_tac_toe_board[1][1] == '2':
        print(f'Second player won')
    elif tic_tac_toe_board[0][1] == '1':
        print(f'First player won')
    elif tic_tac_toe_board[0][1] == '2':
        print(f'Second player won')
    elif tic_tac_toe_board[2][1] == '1':
        print(f'First player won')
    elif tic_tac_toe_board[2][1] == '2':
        print(f'Second player won')
else:
    print(f'Draw!')