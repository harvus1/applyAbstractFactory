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

    def get_total():
        total = 0
        total = total + Pie.get_price()
        total = total + OnionRings.get_price()
        total = total + Milkshake.get_price()
        total = total + ChickenBurger.get_price
        print(total)
        return total
    
    def get_time():
        time = 0
        time = time +Pie.get_time()
        time = time + OnionRings.get_time()
        time = time +Milkshake.get_time()
        time = time +ChickenBurger.get_time()
        print(time)
        return time
        
