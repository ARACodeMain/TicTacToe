# Simple Tic Tac Toe game    برنامج بسيط للعبة
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
turn = 'X'

def show_board():
    print(f'|{board[0]}|{board[1]}|{board[2]}|\t 1 2 3')
    print(f'|{board[3]}|{board[4]}|{board[5]}|\t 4 5 6')
    print(f'|{board[6]}|{board[7]}|{board[8]}|\t 7 8 9')

def winner(board):
    if board[0] == board[1] == board[2] != ' ': return True
    if board[3] == board[4] == board[5] != ' ': return True
    if board[6] == board[7] == board[8] != ' ': return True
    if board[0] == board[3] == board[6] != ' ': return True
    if board[1] == board[4] == board[7] != ' ': return True
    if board[2] == board[5] == board[8] != ' ': return True
    if board[0] == board[4] == board[8] != ' ': return True
    if board[2] == board[4] == board[6] != ' ': return True
    return False

show_board()
while True:
    # Player input
    move = int(input(f'Your turn {turn}')) - 1  # 0:8
    if move >= 0 and move <= 8 and board[move] == ' ':
        board[move] = turn
        show_board()
        # Check winner
        if winner(board):
            print(f'The Winner Is {turn}')
            break
        # Check Draw
        if not ' ' in board:
            print('It is a Draw!')
            break        
        # Switch turns
        if turn == 'X':
            turn = 'O'
        else: turn = 'X'
