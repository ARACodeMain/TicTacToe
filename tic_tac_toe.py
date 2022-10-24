#1 Simple Tic Tac Toe
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
turn = 'X'
def show_board():
    print(f"|{board[0]}|{board[1]}|{board[2]}|  0 1 2")
    print(f"|{board[3]}|{board[4]}|{board[5]}|  3 4 5")
    print(f"|{board[6]}|{board[7]}|{board[8]}|  6 7 8")
    
show_board()

def winner():
    if board[0] == board[1] == board[2] != ' ': return True
    if board[3] == board[4] == board[5] != ' ': return True
    if board[6] == board[7] == board[8] != ' ': return True
    if board[0] == board[3] == board[6] != ' ': return True
    if board[1] == board[4] == board[7] != ' ': return True
    if board[2] == board[5] == board[8] != ' ': return True
    if board[0] == board[4] == board[8] != ' ': return True
    if board[2] == board[4] == board[6] != ' ': return True
    return False

while True:
    move = input(f"Your move {turn} (0:8): ")
    if move in ['0','1','2','3','4','5','6','7','8']:
        move = int(move)
        if board[move] == ' ':
            board[move] = turn
            show_board()
            if winner():
                print(f"The winner is {turn}")
                break
            if ' ' not in board:
                print("It is a Draw XO!")
                break       
            # Switch turn
            if turn == 'X':
                turn = 'O'
            else: turn = 'X'

