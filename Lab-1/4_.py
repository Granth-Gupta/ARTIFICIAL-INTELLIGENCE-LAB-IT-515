def checkTarget(target, rules):
    for conditions, fact in rules:
        if target == fact:
            return conditions
    return []

# Backward chain
def backward_chaining(facts, rules, goal):
    if goal in facts:
        print(f"Fact '{goal}' is directly known.")
        return True
    
    conditions = checkTarget(goal, rules)

    if not conditions:
        print(f"No rule or fact found to prove '{goal}'.")

        return False

    print(f"To prove '{goal}', checking required conditions: {conditions}")

    for cond in conditions:
        proven= backward_chaining(facts, rules, cond)
        if not proven:
            print(f"Failed to prove condition '{cond}'. Hypothesis '{goal}' rejected.")
            return False

    print(f"All conditions met! Goal '{goal}' is PROVEN.")
    return True


facts = [
    "Lights are dim",
    "Engine does not turn over"
]

rules = [
    (["Starter clicks", "Lights are dim"], "Dead Battery"),
    (["Engine turns over", "Fuel tank is empty"], "Out of Gas"),
    (["Engine does not turn over"], "Starter clicks")
]

target = "Dead Battery"

is_proven = backward_chaining(facts, rules, target)
print("===========================")
print(f"Hypothesis '{target}': {'CONFIRMED' if is_proven else 'REJECTED'}\n")