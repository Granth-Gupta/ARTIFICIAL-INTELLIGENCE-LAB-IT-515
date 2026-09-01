# 1. Implement Forward and Backward Chaining for a given knowledge base and compare the reasoning mechanisms.  

def checkFacts(conditions, facts):
    for cond in conditions:
        if cond not in facts:
            return False  
    return True

# FORWARD CHAIN
def forward_chaining(facts, rules, goal):
    facts_changed = True
    
    while facts_changed:
        facts_changed = False
        
        for conditions, result in rules:
            if checkFacts(conditions, facts) and result not in facts:
                facts.append(result)
                facts_changed = True
                
                if result == goal:
                    print(f"Goal '{goal}' successfully reached!")
                    return True
                    
    if goal in facts:
        return True
    else:
        print(f"Could not reach goal '{goal}'.")
        return False
    
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


# Facts
facts = ["A", "B"]

# Rules:
rules = [
    (["A", "B"], "C"),
    (["C", "D"], "E"),
    (["C"], "F"),
    (["F"], "G")
]

target = "F"

# TESTING FORWARD CHAINING

print("===========================")
print("FORWARD CHAINING TEST")
print("===========================")

print("Test")
print("Intitial Facts: ", facts)
print("Taregt: ", target)

forward_chaining(facts, rules, target)

print("===========================")
print("BACKWARD CHAINING TEST")
print("===========================")

# TESTING BACKWARD CHAINING

is_proven = backward_chaining(facts, rules, target)
print("---------------------------")
print(f"Hypothesis '{target}': {'CONFIRMED' if is_proven else 'REJECTED'}\n")