# Sudoku Solver using Backtracking Algorithm

def print_board(board):
    """Prints the Sudoku board in a readable format"""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    """Finds the next empty cell (represented by 0)"""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None


def valid(board, num, pos):
    """Checks if placing num at pos is valid"""
    row, col = pos

    # Check row
    for j in range(len(board[0])):
        if board[row][j] == num and j != col:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][col] == num and i != row:
            return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    """Solves Sudoku using backtracking"""
    find = find_empty(board)
    if not find:
        return True  # Solved
    else:
        row, col = find

    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # Backtrack

    return False


# Example Sudoku board (0 represents empty cells)
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

print("Initial Sudoku Puzzle:\n")
print_board(board)
solve(board)
print("\nSolved Sudoku:\n")
print_board(board)
