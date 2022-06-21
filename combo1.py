from dessert import Dessert
from complement import Complement
from beverage import Beverage
from ice_cream import IceCream
from french_fries import FrenchFries
from coca_cola import CocaCola
from combo_factory import ComboFactory
from burger_builder import BurgerBuilder
from hawaiian_burger import HawaiianBurger


class Combo1(ComboFactory):
    # def __init__(self, name, price, preparation_time):
    #     self.name: str = name
    #     self.price: float = price
    #     self.preparation_time: float = preparation_time

    def create_dessert(self) -> Dessert:
        return IceCream()

    def create_complement(self) -> Complement:
        return FrenchFries()

    def create_beverage(self) -> Beverage:
        return CocaCola()

    def create_burger(self) -> BurgerBuilder:
        return HawaiianBurger()

    def get_total():
        total = 0
        total = total +CocaCola.get_price()
        total = total + FrenchFries.get_price()
        total = total +IceCream.get_price()
        total = total +HawaiianBurger.get_price()
        print(total)
        print("hola")
        return total
    
    def get_time():
        time = 0
        time = time +CocaCola.get_time()
        time = time + FrenchFries.get_time()
        time = time +IceCream.get_time()
        time = time +HawaiianBurger.get_time()
        print(time)
        return time
        
