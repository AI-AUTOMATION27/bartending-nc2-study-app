import random

cocktails = {
    "Pre-Dinner": {
        "Dry Martini": ["60 ml gin", "20 ml dry vermouth", "Garnish with green olives"],
        "Gibson": ["60 ml gin", "20 ml dry vermouth", "Garnish with cocktail onion"],
        "Manhattan": ["45 ml Rye Whisky", "20 ml sweet vermouth", "3 dashes Angostura bitters", "Garnish with cherry"],
        "Cosmpolitan": ["45 ml Vodka", "15 ml Lime juice", "15 ml triple sec", "35 ml Cranberry juice", "Garnish with lemon twist"]
    },
    "After-Dinner": {
        "Brandy Alexander": ["45 ml Brandy", "20 ml creme de cacao", "20 ml cream", "Garnish with nutmeg"],
        "Grasshopper": ["30 ml creme de menthe", "20 ml white creme de cacao", "20 ml light cream", "Garnish with mint"],
        "White Russian": ["30 ml Vodka", "20 ml coffee liqueur", "15 ml light cream", "Garnish with cherry"],
        "Golden Cadillac": ["30 ml Galliano", "20 ml creme de cacao", "20 ml light cream", "Garnish with nutmeg"]
    },
    "Mocktails": {
        "Four Season": ["60 ml orange juice", "60 ml pineapple juice", "60 ml Mango juice", "60 ml Guyabano Juice", "15 ml grenadine", "Garnish with orange slice"],
        "Virgin Mary": ["40 ml tomato juice", "15 ml lemon juice", "3 dash worcestershire sauce", "3 dash tabasco sauce", "pinch of salt and pepper", "Rim with salt and garnish with celery stick"],
        "Virgin Colada": ["60 ml pineapple juice", "20 ml coconut cream", "15 ml lime juice", "Garnish with whipped cream"],
        "Shirley Temple": ["90 ml lemon lime soda", "40 ml ginger ale", "15 ml grenadine", "Garnish with lemon and cherry"]
    },
    "Long/Muddled Drinks": {
        "Harvey Wallbanger": ["45 ml Vodka", "fill glass with orange juice", "25 ml galliano", "Garnish with orange slice and cherry"],
        "Tequila Sunrise": ["45 ml Tequila", "fill glass with orange juice", "15 ml grenadine", "Garnish with orange slice and cherry"],
        "Mojito": ["45 ml white rum", "3 lemon wedge cut", "6-8 mint leaves", "15 ml simple syrup", "fill glass with soda", "Garnish with mint leaves"],
        "Caipirinha": ["60 ml cachaca", "2 teaspoon sugar", "2 slice lemon wedge cut", "Garnish with lemon wedge"]
    },
    "Build Drinks": {
        "Bloody Mary": ["45 ml Vodka", "30 ml tomato juice", "15 ml lemon juice", "3 dash tabasco sauce", "3 dash worcestershire sauce", "pinch of salt and pepper", "Horseradish", "Garnish with celery stick"],
        "Tom Collins": ["45 ml Gin", "15 ml lemon juice", "15 ml simple syrup", "fill glass with soda", "Garnish with orange slice"],
        "Cuba Libre": ["45 ml white rum", "fill glass with cola", "2 slice lemon wedge cut", "Garnish with lemon wedge"],
        "Negroni": ["30 ml gin", "30 ml sweet vermouth", "30 ml campari", "Garnish with orange slice"]
    },
    "Stirred Drinks": {
        "Vodka Martini": ["60 ml vodka", "20 ml dry vermouth", "Garnish with green olives"],
        "Gimlet Straight-up": ["45 ml gin", "15 ml lime juice", "Garnish with lemon slice"],
        "Rob Roy": ["45 ml scotch whisky", "15 ml sweet vermouth", "3 dashes angostura bitters", "Garnish with orange peel"],
        "Perfect Manhattan": ["45 ml rye whisky", "15 ml dry vermouth", "15 ml sweet vermouth", "3 dashes angostura bitters", "Garnish with cherry"]
    },
    "Blended Drinks": {
        "Chi-Chi": ["45 ml vodka", "70 ml pineapple juice", "20 ml coconut cream", "Garnish with pineapple slice and cherry"],
        "Pina Colada": ["45 ml white rum", "4-5 pineapple chunks", "20 ml coconut cream", "Garnish with pineapple slice and cherry"],
        "Frozen Daiquiri": ["45 ml white rum", "15 ml triple sec", "15 ml lime juice", "1 teaspoon sugar", "Garnish with lemon slice and cherry"],
        "Frozen Mango Daiquiri": ["45 ml white rum", "15 ml triple sec", "15 ml lime juice", "3 teaspoon sugar", "1 slice mango", "Garnish with lemon slice and cherry"]
    },
    "Shaken Drinks": {
        "Margarita": ["45 ml tequila", "20 ml lime juice", "20 ml triple sec", "Garnish with lemon slice"],
        "Kamikaze": ["45 ml vodka", "20 ml lime juice", "20 ml triple sec", "Garnish with lemon slice"],
        "Pink Lady": ["45 ml gin", "10 ml grenadine", "15 ml lemon juice", "1 egg white", "Garnish with lemon slice"],
        "Whisky Sour": ["45 ml whisky", "20 ml lemon juice", "15 ml simple syrup", "Garnish with lemon slice"]
    }}

score = 0
total = 0

categories = list(cocktails.keys())
print("Quiz will cover these categories:", ", ".join(categories))
random.shuffle(categories)

for category in categories:
    cocktail = random.choice(list(cocktails[category].keys()))
    correct_ingredients = cocktails[category][cocktail]
    
    print("\n================")
    print("category:", category)
    print("cocktail:", cocktail)

    answer = input("\nType ingredients separated by commas:\n")
    user_ingredients = [x.strip().lower() for x in answer.split(",")]

    correct = [x.lower() for x in correct_ingredients]
    if set(user_ingredients) == set(correct):
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
        print("correct answer:")
        print(", ".join(correct_ingredients))

    total += 1

print("\nFinal Score:", score, "/", total)


