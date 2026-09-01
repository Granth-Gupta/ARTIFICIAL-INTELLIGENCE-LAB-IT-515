from collections import deque

class PuzzleState:
    def __init__(self, board, parent=None, move="", depth=0):
        self.board = board  # Tuple of 9 integers representing 3x3 grid
        self.parent = parent
        self.move = move
        self.depth = depth
        self.zero_idx = self.board.index(0)

    def is_goal(self, goal_board):
        return self.board == goal_board

    def get_neighbors(self):
        neighbors = []
        row, col = divmod(self.zero_idx, 3)
        moves = {
            'UP': (row - 1, col),
            'DOWN': (row + 1, col),
            'LEFT': (row, col - 1),
            'RIGHT': (row, col + 1)
        }

        for move_name, (r, c) in moves.items():
            if 0 <= r < 3 and 0 <= c < 3:
                new_zero_idx = r * 3 + c
                new_board = list(self.board)
                # Swap blank tile (0) with target tile
                new_board[self.zero_idx], new_board[new_zero_idx] = (
                    new_board[new_zero_idx], new_board[self.zero_idx]
                )
                neighbors.append(PuzzleState(tuple(new_board), self, move_name, self.depth + 1))
        return neighbors

    def get_path(self):
        path = []
        curr = self
        while curr.parent:
            path.append(curr.move)
            curr = curr.parent
        return path[::-1]


def solve_bfs(initial_board, goal_board):
    """Breadth-First Search: Uses FIFO Queue"""
    start_state = PuzzleState(initial_board)
    if start_state.is_goal(goal_board):
        return [], 0, 1

    frontier = deque([start_state])
    explored = {initial_board}
    nodes_expanded = 0

    while frontier:
        state = frontier.popleft()
        nodes_expanded += 1

        for neighbor in state.get_neighbors():
            if neighbor.board not in explored:
                if neighbor.is_goal(goal_board):
                    return neighbor.get_path(), neighbor.depth, nodes_expanded
                explored.add(neighbor.board)
                frontier.append(neighbor)

    return None, -1, nodes_expanded


def solve_dfs(initial_board, goal_board, max_depth=20):
    """Depth-First Search (Depth-Limited to prevent infinite loops): Uses LIFO Stack"""
    start_state = PuzzleState(initial_board)
    if start_state.is_goal(goal_board):
        return [], 0, 1

    frontier = [start_state]  # Stack
    explored = set()
    nodes_expanded = 0

    while frontier:
        state = frontier.pop()
        
        if state.board in explored:
            continue
            
        explored.add(state.board)
        nodes_expanded += 1

        if state.is_goal(goal_board):
            return state.get_path(), state.depth, nodes_expanded

        # Depth limit check for practical execution
        if state.depth < max_depth:
            for neighbor in state.get_neighbors():
                if neighbor.board not in explored:
                    frontier.append(neighbor)

    return None, -1, nodes_expanded


# =====================================================================
# EXAMPLE EXECUTION
# =====================================================================
if __name__ == "__main__":
    # 0 represents the empty space
    # Initial state requires a few moves to solve
    initial_board = (1, 2, 3, 
                     4, 0, 6, 
                     7, 5, 8)
    
    goal_board = (1, 2, 3, 
                  4, 5, 6, 
                  7, 8, 0)

    print("--- Solving with BFS ---")
    bfs_path, bfs_depth, bfs_nodes = solve_bfs(initial_board, goal_board)
    print(f"Goal Found! Path: {bfs_path}")
    print(f"Solution Depth: {bfs_depth}, Nodes Expanded: {bfs_nodes}")

    print("\n--- Solving with DFS (Depth Limit = 15) ---")
    dfs_path, dfs_depth, dfs_nodes = solve_dfs(initial_board, goal_board, max_depth=15)
    print(f"Goal Found! Path length: {len(dfs_path) if dfs_path else 'None'}")
    print(f"Solution Depth: {dfs_depth}, Nodes Expanded: {dfs_nodes}")