import copy

class MapColoringCSP:
    def __init__(self, variables, domains, neighbors):
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.backtracks_count = 0
        self.assignments_count = 0

    def is_consistent(self, var, color, assignment):
        """Check if assigning 'color' to 'var' violates any neighbor constraint."""
        for neighbor in self.neighbors[var]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    # -------------------------------------------------------------
    # 1. Pure Backtracking Search
    # -------------------------------------------------------------
    def solve_pure_backtracking(self):
        self.backtracks_count = 0
        self.assignments_count = 0
        assignment = {}

        def backtrack():
            if len(assignment) == len(self.variables):
                return assignment

            # Select unassigned variable
            unassigned = [v for v in self.variables if v not in assignment]
            var = unassigned[0]

            for color in self.domains[var]:
                self.assignments_count += 1
                if self.is_consistent(var, color, assignment):
                    assignment[var] = color
                    result = backtrack()
                    if result:
                        return result
                    del assignment[var]

            self.backtracks_count += 1
            return None

        return backtrack()

    # -------------------------------------------------------------
    # 2. Backtracking with Forward Checking (Constraint Propagation)
    # -------------------------------------------------------------
    def solve_forward_checking(self):
        self.backtracks_count = 0
        self.assignments_count = 0
        assignment = {}
        curr_domains = copy.deepcopy(self.domains)

        def backtrack(domains):
            if len(assignment) == len(self.variables):
                return assignment

            unassigned = [v for v in self.variables if v not in assignment]
            var = unassigned[0]

            for color in list(domains[var]):
                self.assignments_count += 1
                assignment[var] = color
                
                # Perform Constraint Propagation (Forward Checking)
                local_domains = copy.deepcopy(domains)
                local_domains[var] = [color]
                consistent = True

                for neighbor in self.neighbors[var]:
                    if neighbor not in assignment:
                        if color in local_domains[neighbor]:
                            local_domains[neighbor].remove(color)
                            # Dead end detected early if domain empties
                            if not local_domains[neighbor]:
                                consistent = False
                                break

                if consistent:
                    result = backtrack(local_domains)
                    if result:
                        return result

                del assignment[var]

            self.backtracks_count += 1
            return None

        return backtrack(curr_domains)


# Execution & Benchmarking
if __name__ == "__main__":
    # Define Map Regions (Australia)
    variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    colors = ["Red", "Green", "Blue"]
    domains = {var: list(colors) for var in variables}

    # Adjacency Map (Constraints)
    neighbors = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q":  ["NT", "SA", "NSW"],
        "NSW": ["Q", "SA", "V"],
        "V":   ["SA", "NSW"],
        "T":   []
    }

    # Run Pure Backtracking
    csp1 = MapColoringCSP(variables, domains, neighbors)
    sol1 = csp1.solve_pure_backtracking()
    print("--- Pure Backtracking ---")
    print(f"Solution: {sol1}")
    print(f"Assignments Evaluated: {csp1.assignments_count}")
    print(f"Backtracks Triggered: {csp1.backtracks_count}\n")

    # Run Backtracking with Forward Checking
    csp2 = MapColoringCSP(variables, domains, neighbors)
    sol2 = csp2.solve_forward_checking()
    print("--- Backtracking with Forward Checking ---")
    print(f"Solution: {sol2}")
    print(f"Assignments Evaluated: {csp2.assignments_count}")
    print(f"Backtracks Triggered: {csp2.backtracks_count}")