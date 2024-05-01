class Room:
    def __init__(self, number: int, category: chr, daily: float, consumption: list) -> None:
        self.__number = number
        self.__category = category
        self.__daily = daily
        self.__consumption = []

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def category(self) -> chr:
        return self.__category

    @category.setter
    def category(self, category: chr):
        self.__category = category

    @property
    def daily(self) -> float:
        return self.__daily

    @daily.setter
    def daily(self, daily: float):
        self.__daily = daily

    @property
    def consumption(self) -> list:
        return self.__consumption

    @consumption.setter
    def consumption(self, consumption: list):
        self.__consumption = consumption
    def add_consumption(self, consume_item):
        self.__consumption.append(consume_item)

    def list_consumption(self):
        pass
        
    def all_price_consumption(self, price):
        total_price = sum(self.__consumption)
        return total_price

    def clear_consumption(self, consumption):
        self.__consumption = []


    def __str__(self) -> str:
        return f"Código: {self.__number}, Categória: {self.__category}, Diário: R$ {self.__daily}, Consumo: {self.__consumption}"

    def __repr__(self) -> str:
        return f"Código: {self.__number}, Categória: {self.__category}, Diário: R$ {self.__daily}, Consumo: {self.__consumption}"

    def __dict__(self):
        return {'number': self.__number, 'category': self.__category, 'daily': self.__daily, 'consumption': self.__consumption}

    def __iter__(self):
        yield 'number', self.__number
        yield 'category', self.__category
        yield 'daily', self.__daily
        yield 'consumption', self.__consumption