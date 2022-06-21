from dessert import Dessert
from complement import Complement
from beverage import Beverage
from combo_factory import ComboFactory
from pie import Pie
from onion_rings import OnionRings
from milkshake import Milkshake
from burger_builder import BurgerBuilder
from chicken_burger import ChickenBurger


class Combo2(ComboFactory):
    def create_dessert(self) -> Dessert:
        return Pie()

    def create_complement(self) -> Complement:
        return OnionRings()

    def create_beverage(self) -> Beverage:
        return Milkshake()

    def create_burger(self) -> BurgerBuilder:
        return ChickenBurger()
