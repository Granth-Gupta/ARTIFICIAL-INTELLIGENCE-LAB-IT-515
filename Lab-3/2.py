class NQueensCSP:
    def __init__(self, n):
        self.n = n
        self.variables = list(range(n))  # Columns 0 to n-1
        # Domain for each variable (column) is set of available rows [0..n-1]
        self.domains = {col: list(range(n)) for col in range(n)}

    def is_consistent(self, col1, row1, col2, row2):
        """Check if placing queens at (row1, col1) and (row2, col2) causes conflicts."""
        if row1 == row2:  # Same row
            return False
        if abs(row1 - row2) == abs(col1 - col2):  # Same diagonal
            return False
        return True

    def forward_check(self, col, row, assignment, domains):
        """
        Constraint Propagation step:
        Remove inconsistent values from unassigned variables' domains.
        """
        pruned = {}
        for next_col in range(col + 1, self.n):
            pruned[next_col] = []
            for candidate_row in list(domains[next_col]):
                if not self.is_consistent(col, row, next_col, candidate_row):
                    domains[next_col].remove(candidate_row)
                    pruned[next_col].append(candidate_row)
            # If domain becomes empty, forward check fails (dead end)
            if not domains[next_col]:
                return False, pruned
        return True, pruned

    def restore_domains(self, pruned, domains):
        """Restore domains during backtracking step."""
        for col, values in pruned.items():
            domains[col].extend(values)
            domains[col].sort()

    def solve(self):
        assignment = {}
        solutions = []
        
        def backtrack(col, current_domains):
            if col == self.n:
                solutions.append(dict(assignment))
                return

            for row in list(current_domains[col]):
                # Assign queen at column 'col' to 'row'
                assignment[col] = row
                
                # Perform Constraint Propagation (Forward Checking)
                success, pruned = self.forward_check(col, row, assignment, current_domains)
                
                if success:
                    backtrack(col + 1, current_domains)
                
                # Backtrack & restore pruned values
                self.restore_domains(pruned, current_domains)
                del assignment[col]

        backtrack(0, self.domains)
        return solutions

    def print_board(self, solution):
        """Helper to print a visual board for a solution."""
        for r in range(self.n):
            line = []
            for c in range(self.n):
                line.append("Q" if solution[c] == r else ".")
            print(" ".join(line))
        print("\n")


# Execution
if __name__ == "__main__":
    N = 4
    csp = NQueensCSP(N)
    solutions = csp.solve()

    print(f"Total solutions found for {N}-Queens: {len(solutions)}\n")
    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx} (Mapping col -> row: {sol}):")
        csp.print_board(sol)