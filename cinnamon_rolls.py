from dessert import Dessert


class CinnamonRolls(Dessert):
    def __init__(self):
        self.name: str = "Cinnamon Rolls"
        self.price: float = 12.00
        self.time: float = 3.00

    def show_information(self) -> str:
        return self.name
    def get_price(self) -> float:
        return self.price
    
    def get_time(self) -> float:
        return self.time

