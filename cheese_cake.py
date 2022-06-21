from dessert import Dessert


class CheeseCake(Dessert):
    def __init__(self):
        self.name: str = "Cheese Cake"
        self.price: float = 15.00
        self.time: float = 3.00

    def show_information(self) -> str:
        return self.name
