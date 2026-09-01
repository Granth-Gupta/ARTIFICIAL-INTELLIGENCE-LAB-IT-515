# RULES 
rules = [
    (["has_hair"], "mammal"),
    (["has_feathers"], "bird"),
    (["gives_milk"], "mammal"),
    (["lays_eggs", "has_feathers"], "bird")
]

# Check IF all conditions in a rule match the given facts
def checkTarget(target, rules):
    for conditions, fact in rules:
        if target == fact:
            return conditions
    return []

# ANIMAL IDENTIFICATION FUNCTION
def identifyAnimal(given_facts, rules) -> str:
    for conditions, animal_type in rules:
        match = True
        for attribute in conditions:
            if attribute not in given_facts:
                match = False
                break
        if match:
            return animal_type
    return "Current properties are insufficient to identify the animal"

# TESTING WITH USER INPUT
user_input = input("Enter facts separated by spaces (e.g., has_hair eats_meat): ")
given_facts = user_input.strip().split()

result = identifyAnimal(given_facts, rules)
print("Type of animal: ", result)