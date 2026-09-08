import math
import random

def f(x):
    """Objective function to maximize: f(x) = x^3 - 30x^2 + 225x + 100"""
    return x**3 - 30*x**2 + 225*x + 100

def get_neighbors(x, min_bound=0, max_bound=22):
    """Generate neighboring integers within [0, 22]"""
    neighbors = []
    if x > min_bound:
        neighbors.append(x - 1)
    if x < max_bound:
        neighbors.append(x + 1)
    return neighbors

def hill_climbing(start_x):
    """Greedy Hill Climbing algorithm"""
    current_x = start_x
    history = [current_x]
    
    while True:
        neighbors = get_neighbors(current_x)
        best_neighbor = current_x
        best_val = f(current_x)
        
        # Look for a strictly better neighbor
        for n in neighbors:
            if f(n) > best_val:
                best_val = f(n)
                best_neighbor = n
                
        # If no neighbor is strictly better, we reached a local optimum
        if best_neighbor == current_x:
            break
            
        current_x = best_neighbor
        history.append(current_x)
        
    return current_x, f(current_x), history

def simulated_annealing(start_x, initial_temp=5000.0, cooling_rate=0.99, max_iter=2000):
    current_x = start_x
    best_x = current_x
    temp = initial_temp
    history = [current_x]
    
    for _ in range(max_iter):
        neighbors = get_neighbors(current_x)
        next_x = random.choice(neighbors)
        
        delta = f(next_x) - f(current_x)
        
        if delta > 0 or random.random() < math.exp(delta / temp):
            current_x = next_x
            
        if f(current_x) > f(best_x):
            best_x = current_x
            
        history.append(current_x)
        temp *= cooling_rate
        
    return best_x, f(best_x), history

# Set random seed for reproducible results
random.seed(42)

# Run starting from x = 0 (near the local optimum at x = 5)
start_pos = 0

hc_x, hc_f, hc_path = hill_climbing(start_pos)
sa_x, sa_f, sa_path = simulated_annealing(start_pos)

print(f"--- Hill Climbing ---")
print(f"Path taken : {hc_path}")
print(f"Found x    : {hc_x}")
print(f"Max f(x)   : {hc_f}\n")

print(f"--- Simulated Annealing ---")
print(f"Found x    : {sa_x}")
print(f"Max f(x)   : {sa_f}")