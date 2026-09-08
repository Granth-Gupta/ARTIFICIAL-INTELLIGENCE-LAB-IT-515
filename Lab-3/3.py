import math
import copy

class TicTacToe:
    def __init__(self):
        # Empty board initialized as a 1D array of 9 empty spaces
        self.board = [' '] * 9
        self.minimax_nodes = 0
        self.alphabeta_nodes = 0

    def print_board(self, board):
        for row in [board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self, board):
        return [i for i, spot in enumerate(board) if spot == ' ']

    def check_winner(self, board):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for a, b, c in win_conditions:
            if board[a] == board[b] == board[c] and board[a] != ' ':
                return board[a]
        if ' ' not in board:
            return 'Draw'
        return None

    # Standard Minimax
    def minimax(self, board, depth, is_maximizing):
        self.minimax_nodes += 1
        winner = self.check_winner(board)
        
        if winner == 'X':
            return 10 - depth
        elif winner == 'O':
            return depth - 10
        elif winner == 'Draw':
            return 0

        if is_maximizing:
            best_score = -math.inf
            for move in self.available_moves(board):
                board[move] = 'X'
                score = self.minimax(board, depth + 1, False)
                board[move] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for move in self.available_moves(board):
                board[move] = 'O'
                score = self.minimax(board, depth + 1, True)
                board[move] = ' '
                best_score = min(score, best_score)
            return best_score

    # Minimax with Alpha-Beta Pruning
    def alphabeta(self, board, depth, alpha, beta, is_maximizing):
        self.alphabeta_nodes += 1
        winner = self.check_winner(board)
        
        if winner == 'X':
            return 10 - depth
        elif winner == 'O':
            return depth - 10
        elif winner == 'Draw':
            return 0

        if is_maximizing:
            best_score = -math.inf
            for move in self.available_moves(board):
                board[move] = 'X'
                score = self.alphabeta(board, depth + 1, alpha, beta, False)
                board[move] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break  # Cut off branch
            return best_score
        else:
            best_score = math.inf
            for move in self.available_moves(board):
                board[move] = 'O'
                score = self.alphabeta(board, depth + 1, alpha, beta, True)
                board[move] = ' '
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break  # Cut off branch
            return best_score

# Performance Comparison Test
game = TicTacToe()
# Sample mid-game scenario board state
test_board = [
    'X', ' ', 'O',
    ' ', 'X', ' ',
    ' ', ' ', 'O'
]

game.minimax(test_board, 0, True)
game.alphabeta(test_board, 0, -math.inf, math.inf, True)

print(f"Nodes evaluated (Standard Minimax): {game.minimax_nodes}")
print(f"Nodes evaluated (Alpha-Beta Pruning): {game.alphabeta_nodes}")