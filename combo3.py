from dessert import Dessert
from complement import Complement
from beverage import Beverage
from combo_factory import ComboFactory
from cheese_cake import CheeseCake
from cheese_pops import CheesePops
from nectar_juice import NectarJuice
from burger_builder import BurgerBuilder
from fish_burger import FishBurger


class Combo3(ComboFactory):
    def create_dessert(self) -> Dessert:
        return CheeseCake()

    def create_complement(self) -> Complement:
        return CheesePops()

    def create_beverage(self) -> Beverage:
        return NectarJuice()

    def create_burger(self) -> BurgerBuilder:
        return FishBurger()
