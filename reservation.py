from datetime import date

from room import Room
from product import Product


class Reservation:
    def __init__(self, reservation_date_start: date, 
        reservation_date_end: date, client: str, room: Room, status: bool = False) -> None:
        self.__reservation_date_start = reservation_date_start
        self.__reservation_date_end = reservation_date_end
        self.__client = client
        self.__room = room
        self.__status = status
        self.__consumption = list[Product]

    @property
    def reservation_date_start(self):
        return self.__reservation_date_start
        
    @reservation_date_start.setter
    def reservation_date_start(self, reservation_date_start: date):
        self.__reservation_date_start = reservation_date_start

    @property
    def reservation_date_end(self):
        return self.__reservation_date_end
        
    @reservation_date_end.setter
    def reservation_date_end(self, reservation_date_end: date):
        self.__reservation_date_end = reservation_date_end

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

    @property
    def consumption(self):
        return self.__consumption
        
    @consumption.setter
    def consumption(self, consumption: False):
        self.__consumption = consumption

    @property
    def costs(self):
        return sum([item.price for item in self.__consumption])

    def __repr__(self):
        return f"""
        {self.__client} - {self.__room}
        {self.__reservation_date_start.strftime("%d/%m/%Y")} - {self.__reservation_date_end.strftime("%d/%m/%Y")}
        {self.__status}
        {self.__consumption}
        """
    
    def __iter__(self):
        yield 'reservation_date_start', self.__reservation_date_start
        yield 'client', self.__client
        yield 'room', self.__room
        yield 'status', self.__status
        yield 'consumption', self.__consumption
    

    


