class Room:
    def __init__(self, number: int, category: chr, daily: float, consumption: int) -> None:
        self.__number = number
        self.__category = category
        self.__daily = daily
        self.__consumption = consumption
        