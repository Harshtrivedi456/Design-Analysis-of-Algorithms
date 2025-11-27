board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print(row)

def check_winner(symbol):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == symbol:
            return True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == symbol:
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False

player = 'X'
for turn in range(9):  
    print_board()
    print(f"Player {player}'s turn")

    row = int(input("Enter row: "))>
    col = int(input("Enter column: "))

    if board[row][col] != ' ':
        print("Already filled.")
        continue

    board[row][col] = player

    if check_winner(player):
        print_board()
        print(f"Player {player} wins!")
        break

    player = 'O' if player == 'X' else 'X'
else:
    print_board()
    print("Draw")
