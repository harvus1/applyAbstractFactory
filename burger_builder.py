import abc


class BurgerBuilder(metaclass=abc.ABCMeta):

    def burger(self) -> None:
        raise NotImplementedError

    def set_bread(self) -> None:
        raise NotImplementedError

    def set_mayo(self) -> None:
        raise NotImplementedError

    def set_lettuce(self) -> None:
        raise NotImplementedError

    def set_patty(self) -> None:
        raise NotImplementedError

    def set_fish(self) -> None:
        raise NotImplementedError

    def set_chicken(self) -> None:
        raise NotImplementedError

