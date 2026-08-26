# {
#     "if": {"interest": "technology", "skill": "logic", "min_marks": 75},
#     "then": "Bachelor of Science in Computer Science / Software Engineering"
# },
# {
#     "if": {"interest": "healthcare", "skill": "research", "min_marks": 70},
#     "then": "Bachelor of Science in Biotechnology / Pharmacy"
# },
# {
#     "if": {"interest": "business", "skill": "logic", "min_marks": 60},
#     "then": "Bachelor of Business Administration (BBA) in Finance or Analytics"
# },
# {
#     "if": {"interest": "business", "skill": "communication", "min_marks": 60},
#     "then": "Bachelor of Business Administration (BBA) in Marketing / PR"
# },
                    
interests = ["technology", "healthcare", "business"]
skills = ["research","logic","communication"]
recommendations = ["BBA in Marketing", "BBA in Finance", "BSc in Biotechnology", "BSc in CSE"]

text = "Recommended couse is " 

def recommendCourse(marks, skill, interest) -> str:
    if(marks >= 70 and interest != interests[2]):
        if(interest == interests[1] and skill == skills[0]):
            return text + recommendations[2]
        elif(interest == interests[0] and skill == skills[1] and marks >= 75):
            return text + recommendations[3]
    else:
        if(interest == interests[2] and marks >= 60):
            if(skill == skills[1]):
                return text + recommendations[1]
            elif(skill == skills[2]):
                return text + recommendations[0]
    return "Sorry! I don't have a recommanded course for you."
            
print("Test 1")
result1 = recommendCourse(80, "logic", "technology")
print(result1)
print("---------------------------------")

result2 = recommendCourse(60, "communication", "business")
print("Test 2")
print(result2)

# '''
# Test 1
# Recommended couse is BSc in CSE
# ---------------------------------
# Test 2
# Sorry! I don't have a recommanded course for you.

# Granth Gupta@DESKTOP-OH4NI9V MINGW64 /d/NITJ Study/AI Lab
# $ python -u "d:\NITJ Study\AI Lab\Lab-1\2_.py"
# Test 1
# Recommended couse is BSc in CSE
# ---------------------------------
# Test 2
# Recommended couse is BBA in Marketing
# '''