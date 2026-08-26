# FACTS
facts_test_1 = {
    "marks": 80,
    "skill": "logic",
    "interest": "technology"
}

facts_test_2 = {
    "marks": 60,
    "skill": "communication",
    "interest": "business"
}

# RULES
RULES = [
    ({"interest": "technology", "skill": "logic", "min_marks": 75}, "BSc in CSE"),
    ({"interest": "healthcare", "skill": "research", "min_marks": 70}, "BSc in Biotechnology"),
    ({"interest": "business", "skill": "logic", "min_marks": 60}, "BBA in Finance"),
    ({"interest": "business", "skill": "communication", "min_marks": 60}, "BBA in Marketing")
]

# RECOMMENDATION FUNCTION
def recommendCourse(facts: dict) -> str:
    for conditions, course in RULES:
        interest_match = facts.get("interest") == conditions["interest"]
        skill_match = facts.get("skill") == conditions["skill"]
        marks_match = facts.get("marks", 0) >= conditions["min_marks"]

        if interest_match and skill_match and marks_match:
            return "Recommended course is " + course

    return "Sorry! I don't have a recommended course for you."

# TESTING

print("Test 1")
result1 = recommendCourse(facts_test_1)
print(result1)

print("---------------------------------")
print("Test 2")
result2 = recommendCourse(facts_test_2)
print(result2)