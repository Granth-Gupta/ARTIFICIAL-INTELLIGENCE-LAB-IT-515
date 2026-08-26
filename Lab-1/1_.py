# Properties of animals 

mammal = True
bird = False
fish = False
carnivore = True 
pattern = "strips" #---> "strips" , "spots" 
herbivore = False

def identifyAnimal(
        is_mammal, is_bird, is_fish, is_carnivore, _pattern, is_herbivore) -> str:
    if(is_mammal and is_carnivore and (_pattern == "strips") and ( not is_herbivore and not is_fish and not is_bird)):
        return "Tiger"
    elif(is_bird and is_carnivore and (not is_herbivore and not is_fish and not is_mammal)):
        return "Vulture"
    else:
        return  "Current properties are insufficient to identify the animal"

print("Test 1")
result = identifyAnimal(mammal, bird, fish, carnivore, pattern, herbivore)
print(result)

print("----------------------------")
print("Test 2")

result = identifyAnimal(is_mammal=False, is_bird=True, is_fish=False, is_carnivore=True, _pattern="" , is_herbivore=False)
print(result)


'''
OUTPUT:

Test 1
Tiger
----------------------------
Test 2
Current properties are insufficient to identify the animal

Granth Gupta@DESKTOP-OH4NI9V MINGW64 /d/NITJ Study/AI Lab
$ python -u "d:\NITJ Study\AI Lab\Lab-1\1_.py"
Test 1
Tiger
----------------------------
Test 2
Vulture
'''