class KnowledgeBase:
    def __init__(self, facts, rules):
        self.facts = set(facts)
        # Rules are tuples: ([antecedents], consequent)
        # Example: (['A', 'B'], 'C') represents "A AND B -> C"
        self.rules = [ (set(antecedents), consequent) for antecedents, consequent in rules ]

    # -------------------------------------------------------------
    # 1. FORWARD CHAINING (Data-Driven: Facts -> Goal)
    # -------------------------------------------------------------
    def forward_chain(self, goal):
        known_facts = set(self.facts)
        agenda = list(self.facts)
        processed = set()

        # Track unfulfilled antecedents for each rule
        antecedents_left = [set(antecedents) for antecedents, _ in self.rules]

        print("--- Forward Chaining Trace ---")
        while agenda:
            current_fact = agenda.pop(0)

            if current_fact == goal:
                print(f"-> Goal '{goal}' REACHED!")
                return True

            if current_fact not in processed:
                processed.add(current_fact)

                # Check all rules to see if 'current_fact' satisfies a premise
                for i, (antecedents, consequent) in enumerate(self.rules):
                    if current_fact in antecedents_left[i]:
                        antecedents_left[i].remove(current_fact)

                        # If all premises for rule i are fulfilled
                        if len(antecedents_left[i]) == 0:
                            if consequent not in known_facts:
                                known_facts.add(consequent)
                                agenda.append(consequent)
                                print(f"  Applied Rule: {' AND '.join(antecedents)} -> {consequent}")

        print(f"-> Goal '{goal}' CANNOT be proved.")
        return False

    # -------------------------------------------------------------
    # 2. BACKWARD CHAINING (Goal-Driven: Goal -> Facts)
    # -------------------------------------------------------------
    def backward_chain(self, goal, visited=None):
        if visited is None:
            visited = set()
            print("--- Backward Chaining Trace ---")

        # Base case: Goal is an initial fact
        if goal in self.facts:
            print(f"  Fact found: '{goal}' is true.")
            return True

        # Prevent infinite recursive loops
        if goal in visited:
            return False
        visited.add(goal)

        print(f"Attempting to prove goal/sub-goal: '{goal}'")

        # Find rules where the consequent equals current goal
        matching_rules = [ (antecedents, consequent) for antecedents, consequent in self.rules if consequent == goal ]

        for antecedents, _ in matching_rules:
            print(f"  Evaluating Rule: {' AND '.join(antecedents)} -> {goal}")
            
            # Check if all premises of this rule can be proved
            all_premises_true = True
            for premise in antecedents:
                if not self.backward_chain(premise, visited.copy()):
                    all_premises_true = False
                    break  # This rule path failed, try next rule

            if all_premises_true:
                print(f"  Successfully proved '{goal}' using rule premises!")
                return True

        print(f"  Failed to prove sub-goal '{goal}'")
        return False


# =====================================================================
# EXAMPLE EXECUTION
# =====================================================================

# 1. Given Initial Facts
facts = ["A", "B"]

# 2. Given Rules:
# Rule 1: A AND B -> C
# Rule 2: C AND D -> E
# Rule 3: C -> F
# Rule 4: F -> G
rules = [
    (["A", "B"], "C"),
    (["C", "D"], "E"),
    (["C"], "F"),
    (["F"], "G")
]

kb = KnowledgeBase(facts, rules)
target_goal = "G"

# Execute Forward Chaining
fc_result = kb.forward_chain(target_goal)

print("\n" + "="*45 + "\n")

# Execute Backward Chaining
bc_result = kb.backward_chain(target_goal)