from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "cocktail-quiz-secret"

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
    }
}


def build_questions():
    categories = list(cocktails.keys())
    random.shuffle(categories)
    questions = []
    for category in categories:
        cocktail = random.choice(list(cocktails[category].keys()))
        questions.append((category, cocktail))
    return questions


def start_quiz():
    session.clear()
    session["questions"] = build_questions()
    session["index"] = 0
    session["score"] = 0
    session["total"] = 0
    session["message"] = ""

    if session["questions"]:
        category, cocktail = session["questions"][0]
        session["current_category"] = category
        session["current_cocktail"] = cocktail


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "questions" not in session:
            start_quiz()

        category = session.get("current_category")
        cocktail = session.get("current_cocktail")
        answer = request.form.get("answer", "")

        if category and cocktail:
            user_ingredients = [x.strip().lower() for x in answer.split(",") if x.strip()]
            correct = [x.lower() for x in cocktails[category][cocktail]]
            is_correct = set(user_ingredients) == set(correct)

            session["score"] += int(is_correct)
            session["total"] += 1
            session["message"] = "Correct!" if is_correct else f"Incorrect. Correct answer: {', '.join(cocktails[category][cocktail])}"

        next_index = session.get("index", 0) + 1
        if next_index < len(session["questions"]):
            session["index"] = next_index
            category, cocktail = session["questions"][next_index]
            session["current_category"] = category
            session["current_cocktail"] = cocktail
            return render_template(
                "index.html",
                category=category,
                cocktail=cocktail,
                score=session["score"],
                total=session["total"],
                message=session["message"],
            )

        return render_template(
            "index.html",
            finished=True,
            score=session["score"],
            total=session["total"],
            message=session["message"],
        )

    start_quiz()
    category, cocktail = session["questions"][0]
    return render_template(
        "index.html",
        category=category,
        cocktail=cocktail,
        score=session["score"],
        total=session["total"],
        message="",
    )                                                                                                                                                                                                                                                                                            

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
