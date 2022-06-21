from dessert import Dessert
from complement import Complement
from beverage import Beverage
from combo_factory import ComboFactory
from cinnamon_rolls import CinnamonRolls
from hashbrowns import Hashbrowns
from sprite import Sprite
from burger_builder import BurgerBuilder
from bbq_burger import BbqBurger


class Combo4(ComboFactory):
    def create_dessert(self) -> Dessert:
        return CinnamonRolls()

    def create_complement(self) -> Complement:
        return Hashbrowns()

    def create_beverage(self) -> Beverage:
        return Sprite()

    def create_burger(self) -> BurgerBuilder:
        return BbqBurger()
