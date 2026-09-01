import heapq

# -------------------------------------------------------------
# 1. HEURISTIC FUNCTION: Manhattan Distance
# -------------------------------------------------------------
def manhattan_distance(board):
    """
    Calculates sum of distances each tile is from its goal position.
    Ignores blank tile (0).
    """
    distance = 0
    # Map each tile to its target (row, col) in goal_board:
    # 1=(0,0), 2=(0,1), 3=(0,2), 4=(1,0), 5=(1,1), 6=(1,2), 7=(2,0), 8=(2,1)
    goal_positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1)
    }

    for i in range(9):
        tile = board[i]
        if tile != 0:
            current_row, current_col = divmod(i, 3)
            goal_row, goal_col = goal_positions[tile]
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    return distance


# -------------------------------------------------------------
# 2. HELPER: Generate reachable neighboring board states
# -------------------------------------------------------------
def get_neighbors(board):
    neighbors = []
    zero_idx = board.index(0)  # Index of blank space
    row, col = divmod(zero_idx, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # UP, DOWN, LEFT, RIGHT

    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_zero = r * 3 + c
            new_board = list(board)
            # Swap tile with blank space
            new_board[zero_idx], new_board[new_zero] = new_board[new_zero], new_board[zero_idx]
            neighbors.append(tuple(new_board))

    return neighbors


# -------------------------------------------------------------
# 3. A* SEARCH ALGORITHM
# -------------------------------------------------------------
def solve_a_star(start_board, goal_board):
    # Priority Queue stores tuples: (f_score, counter, current_board, g_score)
    # Counter breaks ties in priority queue
    counter = 0
    pq = []

    h_start = manhattan_distance(start_board)
    heapq.heappush(pq, (h_start, counter, start_board, 0))

    g_score = {start_board: 0}
    visited = set()

    # Performance Counters
    nodes_expanded = 0
    nodes_generated = 1  # Includes start node

    while pq:
        f, _, current, g = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        # Check if Goal State is reached
        if current == goal_board:
            solution_depth = g
            solution_cost = g  # Step cost per tile slide = 1
            return nodes_generated, nodes_expanded, solution_depth, solution_cost

        for neighbor in get_neighbors(current):
            tentative_g = g + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                h = manhattan_distance(neighbor)
                f_score = tentative_g + h

                counter += 1
                nodes_generated += 1
                heapq.heappush(pq, (f_score, counter, neighbor, tentative_g))

    return nodes_generated, nodes_expanded, -1, -1


# =============================================================
# MAIN EXECUTION
# =============================================================
if __name__ == "__main__":
    # 0 represents the blank tile
    # 3x3 Initial State:
    # [ 1, 2, 3 ]
    # [ 4, 0, 6 ]
    # [ 7, 5, 8 ]
    initial_state = (
        1, 2, 3,
        4, 0, 6,
        7, 5, 8
    )

    # 3x3 Goal State:
    # [ 1, 2, 3 ]
    # [ 4, 5, 6 ]
    # [ 7, 8, 0 ]
    goal_state = (
        1, 2, 3,
        4, 5, 6,
        7, 8, 0
    )

    # Solve puzzle
    gen, exp, depth, cost = solve_a_star(initial_state, goal_state)

    print("--- A* Search Analysis Results ---")
    print(f"Nodes Generated : {gen}")
    print(f"Nodes Expanded  : {exp}")
    print(f"Solution Depth  : {depth}")
    print(f"Solution Cost   : {cost}")