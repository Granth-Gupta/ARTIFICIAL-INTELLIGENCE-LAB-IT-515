
import heapq
 
print("GREEDY BEST FIRST SEARCH")
print("-----------------------")
 
# Road map
graph = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"C": 8, "B": 5, "F": 6, "E": 2},
    "E": {"C": 10, "D": 2, "F": 3},
    "F": {"D": 6, "E": 3, "G": 1},
    "G": {"F": 1}
}
 
# Heuristic values
h = {
    "A": 13,
    "B": 11,
    "C": 9,
    "D": 5,
    "E": 3,
    "F": 1,
    "G": 0
}
 
start = "A"
goal = "G"
 
# Priority queue
queue = [(h[start], start, [start], 0)]
 
visited = set()
 
while queue:
 
    heuristic, city, path, cost = heapq.heappop(queue)
 
    if city in visited:
        continue
 
    visited.add(city)
 
    print("Expanded:", city, "h =", h[city])
 
    # Goal reached
    if city == goal:
        print("\nPath:", " -> ".join(path))
        print("Total cost:", cost)
        break
 
    # Add neighboring cities
    for next_city in graph[city]:
 
        if next_city not in visited:
 
            new_cost = cost + graph[city][next_city]
            new_path = path + [next_city]
 
            heapq.heappush(
                queue,
                (h[next_city], next_city, new_path, new_cost)
            )
