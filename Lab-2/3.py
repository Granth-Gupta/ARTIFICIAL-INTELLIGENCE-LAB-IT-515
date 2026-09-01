import heapq

# HEURISTIC FUNCTION (Manhattan Distance)
def manhattan_distance(node, goal):
    """
    Calculates Manhattan distance between two grid coordinates (row, col).
    h(n) = |r1 - r2| + |c1 - c2|
    """
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def get_neighbors(node, grid):
    neighbors = []
    rows, cols = len(grid), len(grid[0])
    r, c = node[0], node[1]

    # 4 directional movements: Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_r, new_c = r + dr, c + dc

        # Check grid boundaries and make sure cell is not an obstacle (1)
        if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 0:
            neighbors.append((new_r, new_c))

    return neighbors

def greedy_best_first_search(grid, start, goal):
    # Priority Queue stores tuples: (heuristic_cost, current_node)
    pq = []
    heapq.heappush(pq, (manhattan_distance(start, goal), start))

    visited = {start}
    nodes_expanded = 0

    print("--- Running Greedy Best-First Search ---")
    while pq:
        # Always pop node with smallest heuristic h(n) value
        h_cost, current = heapq.heappop(pq)
        nodes_expanded += 1

        if current == goal:
            print(f"Goal Reached! Total Nodes Expanded: {nodes_expanded}")
            return True, nodes_expanded

        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                h = manhattan_distance(neighbor, goal)
                # Evaluation metric f(n) = h(n)
                heapq.heappush(pq, (h, neighbor))

    print("Goal not reachable!")
    return False, nodes_expanded

def a_star_search(grid, start, goal):
    # Priority Queue stores tuples: (f_cost, current_node)
    pq = []

    # g_score dictionary keeps track of shortest cost from start to each node
    g_score = {start: 0}

    initial_f = 0 + manhattan_distance(start, goal)
    heapq.heappush(pq, (initial_f, start))

    visited = set()
    nodes_expanded = 0

    print("--- Running A* Search ---")
    while pq:
        # Always pop node with smallest total cost f(n) = g(n) + h(n)
        f_cost, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            print(f"Goal Reached! Total Nodes Expanded: {nodes_expanded}")
            return True, nodes_expanded, g_score[current]

        for neighbor in get_neighbors(current, grid):
            # Cost to move to neighbor cell is 1 unit step
            tentative_g = g_score[current] + 1

            # If neighbor reached via cheaper path or not visited before
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                h = manhattan_distance(neighbor, goal)
                f = tentative_g + h  # f(n) = g(n) + h(n)
                heapq.heappush(pq, (f, neighbor))

    print("Goal not reachable!")
    return False, nodes_expanded, float("inf")

# 0 = Free Path, 1 = Obstacle
grid_map = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

start_pos = (0, 0)
goal_pos = (4, 4)

greedy_found, greedy_nodes = greedy_best_first_search(grid_map, start_pos, goal_pos)

print("\n" + "="*45 + "\n")

a_star_found, a_star_nodes, path_cost = a_star_search(grid_map, start_pos, goal_pos)
print(f"Shortest Path Cost: {path_cost}")