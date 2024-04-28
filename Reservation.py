import Room

class Reservation:
    def __init__(self, start_day: int, end_day: int, client: str, room: Room, status: False) -> None:
        self.__start_day = start_day
        self.__end_day = end_day
        self.__client = client
        self.__room = room
        self.__status = status

    @property
    def start_day(self):
        return self.__start_day
        
    @start_day.setter
    def start_day(self, start_day: int):
        self.__star_day = start_day
        
    @property
    def end_day(self):
        return self.__end_day
        
    @end_day.setter
    def end_day(self, end_day: int):
        self.__end_day = end_day

    @property
    def client(self):
        return self.__client
        
    @client.setter
    def client(self, client: str):
        self.__client = client

    @property
    def room(self):
        return self.__room
        
    @room.setter
    def room(self, room: Room):
        self.__room = room

    @property
    def status(self):
        return self.__status
        
    @status.setter
    def status(self, status: False):
        self.__status = status

    

    


