import heapq

def greedy_best_first_search(graph, heuristics, start, goal):
    """
    Implements Greedy Best First Search using a priority queue ordered strictly by h(n).
    
    :param graph: Dict representing adjacency list -> {node: [(neighbor, edge_cost), ...]}
    :param heuristics: Dict representing heuristic values -> {node: h_value}
    :param start: Starting node (e.g., 'A')
    :param goal: Target node (e.g., 'G')
    """
    # Priority Queue stores tuples of: (h(node), node_counter, current_node, path, total_path_cost)
    # node_counter serves as a tie-breaker when two nodes have identical h(n) values.
    counter = 0
    pq = []
    heapq.heappush(pq, (heuristics[start], counter, start, [start], 0))
    
    visited = set()
    expansion_order = []
    
    found_path = None
    final_cost = 0

    while pq:
        h_val, _, current, path, cost = heapq.heappop(pq)
        
        if current in visited:
            continue
            
        # Record expansion details
        visited.add(current)
        expansion_order.append((current, h_val))
        
        # Check if target is reached
        if current == goal:
            found_path = path
            final_cost = cost
            break
            
        # Explore neighbors
        for neighbor, edge_cost in graph.get(current, []):
            if neighbor not in visited:
                counter += 1
                heapq.heappush(
                    pq, 
                    (heuristics[neighbor], counter, neighbor, path + [neighbor], cost + edge_cost)
                )

    # Output Results
    print("--- Cities Expanded (Order & h-values) ---")
    for city, h in expansion_order:
        print(f"City: {city:<12} | h(n) = {h}")
        
    print("\n--- Final Results ---")
    if found_path:
        print(f"Path Found : {' -> '.join(found_path)}")
        print(f"Total Cost : {final_cost}")
    else:
        print("No path found.")

# ==========================================
# EXAMPLE DATA STRUCTURE (Replace with yours)
# ==========================================
if __name__ == "__main__":
    # Define adjacency list: { city: [(neighbor_city, distance), ...] }
    sample_graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('D', 5), ('E', 10)],
        'C': [('F', 3)],
        'D': [('G', 7)],
        'E': [('G', 2)],
        'F': [('D', 2), ('G', 12)],
        'G': []
    }

    # Define straight-line heuristic distances to Goal 'G': { city: h(n) }
    sample_heuristics = {
        'A': 10,
        'B': 6,
        'C': 8,
        'D': 3,
        'E': 2,
        'F': 5,
        'G': 0
    }

    # Run algorithm from 'A' to 'G'
    greedy_best_first_search(sample_graph, sample_heuristics, start='A', goal='G')