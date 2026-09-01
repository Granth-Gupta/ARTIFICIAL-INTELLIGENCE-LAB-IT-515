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
        interest_match = facts["interest"] == conditions["interest"]
        skill_match = facts["skill"] == conditions["skill"]
        marks_match = facts["marks"] >= conditions["min_marks"]

        if interest_match and skill_match and marks_match:
            return "Recommended course is " + course

    return "Sorry! I don't have a recommended course for you."

# TESTING WITH USER INPUT
marks = float(input("Enter your marks: "))
interest = input("Enter your interest (technology, healthcare, business): ")
skill = input("Enter your skill (logic, research, communication): ")

user_facts = {
    "marks": marks,
    "interest": interest,
    "skill": skill
}

result = recommendCourse(user_facts)
print(result)