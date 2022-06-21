from beverage import Beverage


class CocaCola(Beverage):
    def __init__(self):
        self.name: str = "Coca-Cola"
        self.price: float = 8.00
        self.time: float = 6.25

    def show_information(self) -> str:
        return self.name
