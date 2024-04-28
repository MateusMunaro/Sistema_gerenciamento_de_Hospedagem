class Product:
    def __init__(self, code: int, name: str, price: float) -> None:
        self.__code = code
        self.__name = name
        self.__price = price

    @property
    def code(self) -> int:
        return self.__code

    @code.setter
    def code(self, code: int):
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price