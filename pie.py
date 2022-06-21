from dessert import Dessert


class Pie(Dessert):
    def __init__(self):
        self.name: str = "Pie"
        self.price: float = 5.00
        self.time: float = 3.00

    def show_information(self) -> str:
        return self.name
    
    def get_price(self) -> float:
        return self.price
    
    def get_time(self) -> float:
        return self.time

