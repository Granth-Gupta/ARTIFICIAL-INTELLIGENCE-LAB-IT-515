from collections import deque

# 1. BREADTH-FIRST SEARCH (BFS) - Level by Level (FIFO Queue)
def bfs(start, goal):
    queue = deque([start])
    visited = {start}
    nodes_expanded = 0

    while queue:
        current = queue.popleft() # FIFO
        nodes_expanded += 1

        if current == goal:
            return True, nodes_expanded

        for neighbor in [current + 1, current * 2]:
            if neighbor not in visited and neighbor <= goal:
                visited.add(neighbor)
                queue.append(neighbor)

    return False, nodes_expanded

# DEPTH-FIRST SEARCH (DFS) - Deepest First (LIFO Stack)
def dfs(start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        current = stack.pop() 
        
        if current in visited:
            continue
            
        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return True, nodes_expanded

        for neighbor in [current + 1, current * 2]:
            if neighbor not in visited and neighbor <= goal:
                stack.append(neighbor)

    return False, nodes_expanded

# RUNNING THE SEARCH
start_state = 1
goal_state = 10

# Test BFS
bfs_found, bfs_count = bfs(start_state, goal_state)
print(f"BFS Goal Found: {bfs_found} | Total Nodes Expanded: {bfs_count}")

# Test DFS
dfs_found, dfs_count = dfs(start_state, goal_state)
print(f"DFS Goal Found: {dfs_found} | Total Nodes Expanded: {dfs_count}")