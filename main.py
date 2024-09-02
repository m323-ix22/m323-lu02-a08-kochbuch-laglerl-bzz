import json
"""
    Solved Recipe adjustment
"""


def load_recipe(recipe):
    return json.loads(recipe)


def adjust_recipe(recipe, persons):
    factor = persons / recipe['servings']
    adjusted_ingredients = {ingredient: amount * factor for ingredient, amount in recipe['ingredients'].items()}
    return {
        'title': recipe['title'],
        'ingredients': adjusted_ingredients,
        'servings': persons
    }


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, '
                   '"Minced Meat": 500}, "servings": 4}')
