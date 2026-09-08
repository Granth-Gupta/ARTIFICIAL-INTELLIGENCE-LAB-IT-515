game_tree = [[[3, 5], [6, 9]], [[1, 2], [0, -1]]]

minimax_nodes_visited = 0
alphabeta_nodes_visited = 0

# 1. Minimax Algorithm
def minimax(node, is_maximizing):
    global minimax_nodes_visited
    minimax_nodes_visited += 1

    # Base case: Leaf node
    if isinstance(node, int):
        return node

    if is_maximizing:
        best_value = float('-inf')
        for child in node:
            value = minimax(child, False)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for child in node:
            value = minimax(child, True)
            best_value = min(best_value, value)
        return best_value


# 2. Alpha-Beta Pruning Algorithm
def alpha_beta(node, alpha, beta, is_maximizing):
    global alphabeta_nodes_visited
    alphabeta_nodes_visited += 1

    # Base case: Leaf node
    if isinstance(node, int):
        return node

    if is_maximizing:
        best_value = float('-inf')
        for child in node:
            value = alpha_beta(child, alpha, beta, False)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break  # Beta cut-off (Prune remaining branches)
        return best_value
    else:
        best_value = float('inf')
        for child in node:
            value = alpha_beta(child, alpha, beta, True)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta <= alpha:
                break  # Alpha cut-off (Prune remaining branches)
        return best_value


# Run Minimax
minimax_result = minimax(game_tree, True)

# Run Alpha-Beta Pruning
alphabeta_result = alpha_beta(game_tree, float('-inf'), float('inf'), True)

# Output Results
print(f"Minimax Result: {minimax_result}")
print(f"Minimax Total Nodes Visited: {minimax_nodes_visited}")
print("-" * 40)
print(f"Alpha-Beta Pruning Result: {alphabeta_result}")
print(f"Alpha-Beta Pruning Total Nodes Visited: {alphabeta_nodes_visited}")
print("-" * 40)
print(f"Comparison: Alpha-Beta Pruning visited {minimax_nodes_visited - alphabeta_nodes_visited} fewer nodes!")