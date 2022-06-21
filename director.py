from burger_builder import BurgerBuilder


class Director:
    def __init__(self) -> None:
        self._burger_builder = None

    @property
    def burger_builder(self) -> BurgerBuilder:
        return self._burger_builder

    @burger_builder.setter
    def burger_builder(self, burger_builder: BurgerBuilder) -> None:
        self._burger_builder = burger_builder


    def make_hawaiian_burger(self) -> None:
        self.burger_builder.set_bread()
        self.burger_builder.set_mayo()
        self.burger_builder.set_patty()

    def make_chicken_sandwich(self) -> None:
        self.burger_builder.set_bread()
        self.burger_builder.set_mayo()
        self.burger_builder.set_chicken()
        self.burger_builder.set_lettuce()

    def build_burger(self) -> None:
        self.burger_builder.set_bread()
        self.burger_builder.set_fish()
        self.burger_builder.set_mayo()
        self.burger_builder.set_patty()
        self.burger_builder.set_chicken()
        self.burger_builder.set_lettuce()



