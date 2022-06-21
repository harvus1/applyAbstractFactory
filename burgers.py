from typing import Any


class Burgers():
    def __init__(self) -> None:
        self.ingredients = []

    def add(self, ingredient: Any ) -> None:
        self.ingredients.append(ingredient)

    def list_ingredients(self) -> None:
        print(f"Burger Ingredients: {', ' .join(self.ingredients)}", end="")