# pre-defining
n = 1
print("Please, add information for at least 2 days!")
# checklist for consumed
print(f"Day {n} - Did you consume: (please, write 0 for 'no' and 1 for 'yes')")
diary_food = {}
alcohol = input("- alcohol: ")
caffeine = input("- caffeine: ")
red_meat = input("- red meat: ")
gluten = input("- gluten: ")
sugar = input("- sugar: ")
diary_food = {"alcohol": alcohol, "caffeine": caffeine, "red meat": red_meat, "gluten": gluten, "sugar": sugar}

# checklist for symptoms
print(f"Day {n} - Did you experience any of those symptoms today: (please, write 0 for 'no' and 1 for 'yes')")
diary_symptoms = {}
pain = input("- pain: ")
bleeding = input("- bleeding: ")
nausea = input("- nausea: ")
bloating = input("- bloating: ")
fatigue = input("- fatigue: ")
diary_symptoms = {"pain": pain, "bleeding": bleeding, "nausea": nausea, "bloating": bloating, "fatigue": fatigue}

# for c in day_n_s:
#     if day_n_s[c] == "y":
#         print(c)

# adding food and symptoms in a diary - a list for each
# adds new key in diary until alcohol == ''
diary = {n: [diary_food, diary_symptoms]}
while True:
    n += 1
    print(f"Day {n} - Did you consume: (please, write 0 for 'no' and 1 for 'yes', leave blank to quit)")
    alcohol = input("- alcohol: ")

    if alcohol == '': break  # !!! why doesn't work with break on next line?!

    caffeine = input("- caffeine: ")
    red_meat = input("- red meat: ")
    gluten = input("- gluten: ")
    sugar = input("- sugar: ")

    diary_food = {"alcohol": alcohol, "caffeine": caffeine, "red meat": red_meat, "gluten": gluten, "sugar": sugar}

    print(f"Day {n} - Did you experience any of those symptoms today: (please, write 0 for 'no' and 1 for 'yes')")
    pain = input("- pain: ")
    bleeding = input("- bleeding: ")
    nausea = input("- nausea: ")
    bloating = input("- bloating: ")
    fatigue = input("- fatigue: ")

    diary_symptoms = {"pain": pain, "bleeding": bleeding, "nausea": nausea, "bloating": bloating, "fatigue": fatigue}

    diary[n] = [diary_food, diary_symptoms]

# print(diary)
q = 1

print(q)

symptoms_all = []
food_all = []

for p in range(1, n):
    #    if q in diary[p][1]:
    #        print(8)
    #    for symptom in diary[p][1].values():
    #        if symptom==1:
    #            print(symptom)
    for key, value in diary_symptoms.items():
        if value == "1":
            symptoms_all.append(key)

    symptoms_unique = []
    for i in symptoms_all:
        if i not in symptoms_unique:
            symptoms_unique.append(i)

    print(f"On day {p} you have experienced {symptoms_unique}")

    for key, value in diary_food.items():
        if value == "1":
            food_all.append(key)

    food_unique = []
    for j in food_all:
        if i not in food_unique:
            food_unique.append(i)
