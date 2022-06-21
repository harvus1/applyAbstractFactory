from beverage import Beverage


class Milkshake(Beverage):
    def __init__(self):
        self.name: str = "Milkshake"
        self.price: float = 15.00
        self.time: float = 60.00

    def show_information(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price
    
    def get_time(self) -> float:
        return self.time

    


