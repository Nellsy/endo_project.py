# day counter
n = 1

# pre-defined checker
add_day = True
diary_symptoms = {}
diary_food = {}

symptoms = {}
food = {}

while add_day:

    food = []
    symptoms = []

    if n <= 2:
        print("Please, add information for at least 2 days!")

    # checklist for consumed
    print(f"Day {n} - Did you consume: (please, write 0 for 'no' and 1 for 'yes')")
    food_day = {}
    alcohol = input("- alcohol: ")
    caffeine = input("- caffeine: ")
    red_meat = input("- red meat: ")
    gluten = input("- gluten: ")
    sugar = input("- sugar: ")
    food_day = {"alcohol": alcohol, "caffeine": caffeine, "red meat": red_meat, "gluten": gluten, "sugar": sugar}

    # checklist for symptoms
    print(f"Day {n} - Did you experience any of those symptoms today: (please, write 0 for 'no' and 1 for 'yes')")
    symptoms_day = {}
    pain = input("- pain: ")
    bleeding = input("- bleeding: ")
    nausea = input("- nausea: ")
    bloating = input("- bloating: ")
    fatigue = input("- fatigue: ")
    symptoms_day = {"pain": pain, "bleeding": bleeding, "nausea": nausea, "bloating": bloating, "fatigue": fatigue}

    # diary[n] = [diary_food, diary_symptoms]
    # diary = {n: [diary_food, diary_symptoms]}

    # symptoms[n] = [symptoms_day]

    for key, value in symptoms_day.items():
        if value == "1":
            if key not in symptoms:
                symptoms.append(key)

    diary_symptoms[n] = symptoms

    for key, value in food_day.items():
        if value == "1":
            if key not in food:
                food.append(key)

    diary_food[n] = food

    n += 1

    if n > 2:
        print(f"Would you like to add information for day {n}?")
        q = input("Write 0 for 'no' and 1 for 'yes': ")
        if q == "0":
            add_day = False


for l in (1, n-1):
    if l == 1:
        print(f"On Day {l} you have experienced {diary_symptoms[l]}. There are no entries for previous day.")
    # print(diary_symptoms[l])
    else:
        print(f"On Day {l} you have experienced {diary_symptoms[l]}. Yesterday you have consumed {diary_food[l-1]}.")

q = 1
print(q)
