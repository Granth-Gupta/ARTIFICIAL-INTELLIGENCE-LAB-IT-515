class AOStar:
    def __init__(self, graph, heuristics):
        self.graph = graph
        self.H = heuristics
        self.solution_tree = {}

    def get_heuristic(self, node):
        return self.H.get(node, 0)

    def compute_cost(self, node):
        """Calculates the minimum cost among all available OR branches for a node."""
        if node not in self.graph or not self.graph[node]:
            return self.get_heuristic(node), []

        min_cost = float('inf')
        best_branch = []

        for branch in self.graph[node]:
            # Each edge cost = 1. Cost = sum(1 + h(child)) for all children in AND branch
            branch_cost = sum((1 + self.get_heuristic(child)) for child in branch)
            if branch_cost < min_cost:
                min_cost = branch_cost
                best_branch = branch

        return min_cost, best_branch

    def solve(self, root):
        """Iteratively updates costs and expands nodes until convergence."""
        while True:
            changed = False
            
            # Post-order traversal helper to update children before parents
            def update_node(node):
                nonlocal changed
                if node not in self.graph or not self.graph[node]:
                    return

                # 1. First recurse into currently selected children
                if node in self.solution_tree:
                    for child in self.solution_tree[node]:
                        update_node(child)

                # 2. Re-compute best cost for current node
                new_cost, best_branch = self.compute_cost(node)
                
                if new_cost != self.H[node] or self.solution_tree.get(node) != best_branch:
                    self.H[node] = new_cost
                    self.solution_tree[node] = best_branch
                    changed = True

            update_node(root)
            
            # Stop when no heuristic values or path choices change anymore
            if not changed:
                break

        return self.H[root]

    def print_solution(self, node, depth=0):
        indent = "  " * depth
        if node in self.solution_tree and self.solution_tree[node]:
            children = self.solution_tree[node]
            print(f"{indent}{node} -> {children}")
            for child in children:
                self.print_solution(child, depth + 1)
        else:
            print(f"{indent}{node} (Leaf Node, h = {self.get_heuristic(node)})")


# Initial Heuristics
heuristics = {
    'A': 6, 'B': 5, 'C': 2, 'D': 8,
    'E': 3, 'F': 4, 'G': 5, 'H': 7, 'J': 1
}

# Graph representation
graph = {
    'A': [['B'], ['C', 'D']],
    'B': [['G', 'H']],
    'C': [['J']],
    'D': [['E', 'F']]
}

solver = AOStar(graph, heuristics)
final_cost = solver.solve('A')

print(f"FINAL OPTIMAL COST FOR ROOT 'A': {final_cost}\n")
print("FINAL SOLUTION GRAPH:")
solver.print_solution('A')