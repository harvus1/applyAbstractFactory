from burger_builder import BurgerBuilder
from burgers import Burgers

class ConcreteBurger(BurgerBuilder):
    def __init__(self, burger_name):
        self._burger = None
        self.burger_name: str = burger_name
        self.reset()


    def reset(self) -> None:
        self._burger = Burgers()

    @property
    def burger(self) -> Burgers:
        burger = self._burger
        self.reset()
        return burger

    def set_bread(self) -> None:
        self._burger.add("Bread")

    def set_mayo(self) -> None:
        self._burger.add("Mayonnaise")

    def set_lettuce(self) -> None:
        self._burger.add("Lettuce")

    def set_patty(self) -> None:
        self._burger.add("Patty")

    def set_fish(self) -> None:
        self._burger.add("Fish")

    def set_chicken(self) -> None:
        self._burger.add("Chicken")


