from complement import Complement


class CheesePops(Complement):
    def __init__(self):
        self.name: str = "Cheese Pops"
        self.price: float = 6.00
        self.time: float = 2.50

    def show_information(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price
    
    def get_time(self) -> float:
        return self.time
