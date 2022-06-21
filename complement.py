import abc


class Complement(metaclass=abc.ABCMeta):
    def show_information(self) -> str:
        raise NotImplementedError