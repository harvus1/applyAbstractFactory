from dessert import Dessert
from complement import Complement
from beverage import Beverage
from burger_builder import BurgerBuilder
import abc


class ComboFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_dessert(self) -> Dessert:
        raise NotImplementedError

    def create_complement(self) -> Complement:
        raise NotImplementedError

    def create_beverage(self) -> Beverage:
        raise NotImplementedError

    def create_burger(self) -> BurgerBuilder:
        raise NotImplementedError
