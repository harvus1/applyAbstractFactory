from beverage import Beverage


class Sprite(Beverage):
    def __init__(self):
        self.name: str = "Sprite"
        self.price: float = 8.00
        self.time: float = 4.25

    def show_information(self) -> str:
        return self.name