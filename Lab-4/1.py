import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Ordinary Minimax
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O": return 1
    if winner == "X": return -1
    if is_full(board): return 0

    if is_maximizing:
        max_eval = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[r][c] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[r][c] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

# Minimax with Alpha-Beta Pruning
def alpha_beta(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == "O": return 1
    if winner == "X": return -1
    if is_full(board): return 0

    if is_maximizing:
        max_eval = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "O"
                    eval = alpha_beta(board, depth + 1, alpha, beta, False)
                    board[r][c] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "X"
                    eval = alpha_beta(board, depth + 1, alpha, beta, True)
                    board[r][c] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = "O"
                move_val = alpha_beta(board, 0, -math.inf, math.inf, False)
                board[r][c] = " "
                if move_val > best_val:
                    best_val = move_val
                    best_move = (r, c)
    return best_move