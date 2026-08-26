def checkFacts(conditions, facts):
    for cond in conditions:
        if(cond in facts):
            return True
    return False

def forward_chaining(facts, rules, goal):
    facts_changed = True
    
    while facts_changed:
        facts_changed = False
        
        for conditions, result in rules:
            if checkFacts(conditions, facts) and result not in facts:
                facts.append(result)
                print("New fact: " + result)
                facts_changed = True
                
                if result == goal:
                    print(f"Goal '{goal}' successfully reached!")
                    return True
                    
    if goal in facts:
        return True
    else:
        print(f"Could not reach goal '{goal}'.")
        return False

known_facts = ["has_fever", "has_cough"]
print("Intitial Facts: ", known_facts)

rules = [
    (["has_fever", "has_cough"], "has_flu"),
    (["has_flu"], "needs_rest")
]
target = "needs_rest"

forward_chaining(known_facts, rules, target)