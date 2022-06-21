from burger_builder import BurgerBuilder


class FishBurger(BurgerBuilder):
    def __init__(self):
        self.name: str = "Fish Burger"
        self.price: float = 12.00
        self.time: float = 3.00

    def show_information(self) -> str:
        return self.name