from dessert import Dessert


class IceCream(Dessert):
    def __init__(self):
        self.name: str = "Ice Cream"
        self.price: float = 8.00
        self.time: float = 13.00

    def show_information(self) -> str:
        return self.name
