from complement import Complement


class OnionRings(Complement):
    def __init__(self):
        self.name: str = "Onion Rings"
        self.price: float = 8.00
        self.time: float = 12.50

    def show_information(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price
    
    def get_time(self) -> float:
        return self.time
