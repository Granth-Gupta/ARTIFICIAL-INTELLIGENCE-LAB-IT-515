# FACTS  
facts_test_1 = ["mammal", "carnivore", "strips"]  
facts_test_2 = ["bird", "carnivore"]  

# RULES  
rules = [  
(["mammal", "carnivore", "strips"], "Tiger"),  
(["bird", "carnivore"], "Vulture"),  
(["mammal", "herbivore", "strips"], "Zebra")  
]  

# Check IF all conditions in a rule match the given facts  
def checkTarget(target, rules):  
    for conditions, fact in rules:  
        if target == fact:  
            return conditions  
    return []  

# ANIMAL IDENTIFICATION FUNCTION  
def identifyAnimal(given_facts, rules) -> str:  
    for conditions, animal in rules:  
        match = True 
        
        for attribute in conditions:  
            if attribute not in given_facts:  
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