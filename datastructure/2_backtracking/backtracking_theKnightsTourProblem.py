def is_safe(x, y, board, N):
    """
    Check if (x, y) is a valid position on the board and not yet visited.
    """
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def print_board(board):
    """
    Print the chessboard with the step numbers of the knight's moves.
    """
    for row in board:
        print(" ".join(str(cell).rjust(2, ' ') for cell in row))
    print()

def knight_tour_util(x, y, move_i, board, x_moves, y_moves, N):
    """
    Recursive utility to perform the knight's tour using backtracking
    Args:
        x, y: current position of knight
        move_i: current move number
        board: current board state with move numbers
        x_moves, y_moves: possible moves for knight
        N: board size
    Returns:
        True if the tour is complete, else False for backtracking
    """
    if move_i == N * N:
        return True  # All cells are visited

    # Try all next moves from the current coordinate x, y
    for k in range(8):
        next_x = x + x_moves[k]
        next_y = y + y_moves[k]
        if is_safe(next_x, next_y, board, N):
            board[next_x][next_y] = move_i  # mark move number
            if knight_tour_util(next_x, next_y, move_i + 1, board, x_moves, y_moves, N):
                return True
            # Backtracking
            board[next_x][next_y] = -1
    return False

def knight_tour(N):
    """
    Initialize the board and start the knight's tour backtracking
    Args:
        N: size of the chessboard NxN
    """
    board = [[-1 for _ in range(N)] for _ in range(N)]

    # Knight's possible 8 moves
    x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

    # Starting position
    board[0][0] = 0

    if not knight_tour_util(0, 0, 1, board, x_moves, y_moves, N):
        print("No solution exists.")
        return False
    else:
        print("Knight's tour solution:")
        print_board(board)
        return True

# Example usage:
knight_tour(5)
