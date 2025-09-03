def print_board(board):
    """Prints the current board configuration."""
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()

def is_safe(board, row, col, N):
    """
    Checks if it's safe to place a queen at board[row][col].
    This means no queen can attack this cell horizontally, vertically, or diagonally.
    """
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            print(f"Queen at ({row},{col}) conflicts horizontally with queen at ({row},{i})")
            return False

    # Check upper diagonal on the left side
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            print(f"Queen at ({row},{col}) conflicts upper diagonally with queen at ({i},{j})")
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row + 1, col - 1
    while i < N and j >= 0:
        if board[i][j] == 1:
            print(f"Queen at ({row},{col}) conflicts lower diagonally with queen at ({i},{j})")
            return False
        i += 1
        j -= 1

    print(f"Queen can be placed at ({row},{col}) safely")
    return True

def solve_n_queens_util(board, col, N):
    """
    Recursively places queens on the board column by column using backtracking.
    Prints the board at every recursive stage.
    """
    if col >= N:
        print("Found one solution!\nFinal board:")
        print_board(board)
        return True

    res = False  # To check if solution exists
    for row in range(N):
        print(f"Trying to place queen at row {row}, column {col}")
        if is_safe(board, row, col, N):
            board[row][col] = 1  # Place queen
            print_board(board)
            # Recursively place queen in next column
            res = solve_n_queens_util(board, col + 1, N) or res
            # If placing queen at board[row][col] doesn't solve,
            # Remove queen (Backtrack)
            board[row][col] = 0
            print(f"Backtracking from ({row},{col})")
            print_board(board)
    return res

def solve_n_queens(N):
    """
    Initializes the board and starts the backtracking process.
    Prints the solution if one exists.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_n_queens_util(board, 0, N):
        print("No solution exists for N =", N)
    else:
        print("Above is one solution to the N Queen problem.")

# Example: Solve for N=4
solve_n_queens(4)
