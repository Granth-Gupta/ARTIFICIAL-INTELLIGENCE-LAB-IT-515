# FACTS 
facts_test_1 = {
    "is_mammal": True,
    "is_bird": False,
    "is_fish": False,
    "is_carnivore": True,
    "pattern": "strips",
    "is_herbivore": False
}

facts_test_2 = {
    "is_mammal": False,
    "is_bird": True,
    "is_fish": False,
    "is_carnivore": True,
    "pattern": "",
    "is_herbivore": False
}


# RULE BASE
rules = [
    ({"is_mammal": True, "is_carnivore": True, "pattern": "strips"}, "Tiger"),
    ({"is_bird": True, "is_carnivore": True, "is_herbivore": False}, "Vulture"),
    ({"is_mammal": True, "is_herbivore": True, "pattern": "strips"}, "Zebra")
]

# Check IF all conditions in a rule match the given facts
def checkTarget(target, rules):
    for conditions, fact in rules:
        if target == fact:
            return conditions
    return {}

# ANIMAL IDENTIFICATION FUNCTION
def identifyAnimal(given_facts, rules) -> str:
    for conditions, animal in rules:
        match = True
        
        for attribute, value in conditions.items():
            if given_facts.get(attribute) != value:
                match = False
                break
                
        if match:
            return animal
            
    return "Current properties are insufficient to identify the animal"


# TESTING
print("Test 1")
result = identifyAnimal(facts_test_1, rules)
print(result)

print("----------------------------")
print("Test 2")
result = identifyAnimal(facts_test_2, rules)
print(result)