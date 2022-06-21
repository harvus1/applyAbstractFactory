from complement import Complement


class Hashbrowns(Complement):
    def __init__(self):
        self.name: str = "Hashbrowns"
        self.price: float = 10.00
        self.time: float = 2.50

    def show_information(self) -> str:
        return self.name