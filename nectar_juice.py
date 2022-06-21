from beverage import Beverage


class NectarJuice(Beverage):
    def __init__(self):
        self.name: str = "Nectar Juice"
        self.price: float = 8.00
        self.time: float = 4.25

    def show_information(self) -> str:
        return self.name
