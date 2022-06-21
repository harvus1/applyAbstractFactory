import abc


class Beverage(metaclass=abc.ABCMeta):
    def show_information(self) -> str:
        raise NotImplementedError