# KNOWN FACTS
known_facts_1 = ["has_fever", "has_cough"]
known_facts_2 = ["has_cough"]

# RULES
rules = [
    (["has_fever", "has_cough"], "has_flu"),
    (["has_flu"], "needs_rest")
]

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

# TESTING
    
target = "needs_rest"

print("Test 1")
print("Intitial Facts: ", known_facts_1)
print("Taregt: ", target)

forward_chaining(known_facts_1, rules, target)

target = "has_flu"

print("-------------------------")

print("Test 2")
print("Intitial Facts: ", known_facts_2)
print("Taregt: ", target)

forward_chaining(known_facts_2, rules, target)