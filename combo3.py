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

    def get_total():
        total = 0
        total = total +CheeseCake.get_price()
        total = total + CheesePops.get_price()
        total = total +NectarJuice.get_price()
        total = total +FishBurger.get_price()
        print(total)
        print("hola")
        return total
    
    def get_time():
        time = 0
        time = time +CheeseCake.get_time()
        time = time + CheesePops.get_time()
        time = time +NectarJuice.get_time()
        time = time +FishBurger.get_time()
        print(time)
        return time
