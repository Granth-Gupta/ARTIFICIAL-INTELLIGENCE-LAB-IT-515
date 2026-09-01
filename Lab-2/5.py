# =====================================================================
# 1. KNOWLEDGE BASE: Graph Edge Costs & Heuristic Values h(n)
# =====================================================================

# Edge weights representing actual step costs between connected cities
edge_costs = {
    ('A', 'C'): 2,
    ('C', 'E'): 4,
    ('E', 'F'): 3,
    ('F', 'G'): 2,
    ('C', 'B'): 1,
    ('B', 'D'): 2,
    ('D', 'E'): 3
}

# Heuristic estimates h(n) to Goal city G
heuristic = {
    'A': 8,
    'B': 6,
    'C': 7,
    'D': 4,
    'E': 3,
    'F': 1,
    'G': 0
}


# =====================================================================
# 2. EVALUATION FUNCTION
# =====================================================================
def evaluate_path(path_name, path):
    print(f"\n{'='*75}")
    print(f"EVALUATING: {path_name} ( Path: {' -> '.join(path)} )")
    print(f"{'='*75}")
    
    # Step 1: Calculate cumulative path cost g(n) for each node
    g_values = {}
    g_values[path[0]] = 0  # Start node A has g(A) = 0
    
    for i in range(1, len(path)):
        prev_node = path[i-1]
        curr_node = path[i]
        edge = (prev_node, curr_node)
        
        # Add edge cost to previous g(n) value
        g_values[curr_node] = g_values[prev_node] + edge_costs[edge]
        
    total_path_cost = g_values[path[-1]]
    
    # Header for tabular output
    print(f"{'City (n)':<10} | {'g(n)':<8} | {'h(n)':<8} | {'f(n)=g+h':<10} | {'Actual Remaining':<18} | {'Is h(n) > Remaining?'}")
    print("-" * 80)
    
    admissible_violation = False
    
    # Step 2: Evaluate metrics at each city along the path
    for city in path:
        g = g_values[city]
        h = heuristic[city]
        f = g + h
        
        # Actual cost remaining from current city to Goal G
        actual_remaining = total_path_cost - g
        
        # Check if heuristic overestimates actual remaining cost
        overestimated = h > actual_remaining
        if overestimated:
            admissible_violation = True
            
        overestimate_str = "YES (Inadmissible)" if overestimated else "No (Admissible)"
        
        print(f"{city:<10} | {g:<8} | {h:<8} | {f:<10} | {actual_remaining:<18} | {overestimate_str}")
        
    print("-" * 80)
    print(f"TOTAL PATH COST: {total_path_cost}")
    
    if admissible_violation:
        print("WARNING: h(n) became larger than actual remaining cost at one or more nodes!")
    else:
        print("SUCCESS: h(n) NEVER exceeded actual remaining cost on this path.")
        
    return total_path_cost


# =====================================================================
# MAIN EXECUTION
# =====================================================================
if __name__ == "__main__":
    # Define paths
    path1 = ['A', 'C', 'E', 'F', 'G']
    path2 = ['A', 'C', 'B', 'D', 'E', 'F', 'G']

    # Run evaluations
    cost1 = evaluate_path("Path 1", path1)
    cost2 = evaluate_path("Path 2", path2)