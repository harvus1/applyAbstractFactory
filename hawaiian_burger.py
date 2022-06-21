from burger_builder import BurgerBuilder


class HawaiianBurger(BurgerBuilder):
    def __init__(self):
        self.name: str = "Cinnamon Rolls"
        self.price: float = 12.00
        self.time: float = 3.00

    def show_information(self) -> str:
        return self.name