import Room

class Reservation:
    def __init__(self, start_day: int, end_day: int, client: str, room: Room, status: False) -> None:
        self.__start_day = start_day
        self.__end_day = end_day
        self.__client = client
        self.__room = room
        self.__status = status

    
