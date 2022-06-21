from complement import Complement


class FrenchFries(Complement):
    def __init__(self):
        self.name: str = "French Fries"
        self.price: float = 8.00
        self.time: float = 8.00

    def show_information(self) -> str:
        return self.name