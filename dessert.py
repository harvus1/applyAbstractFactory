import abc


class Dessert(metaclass=abc.ABCMeta):
    def show_information(self) -> str:
        raise NotImplementedError