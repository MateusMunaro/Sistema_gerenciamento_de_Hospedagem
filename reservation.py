from datetime import date

from room import Room


class Reservation:
    def __init__(self, reservation_date_start: date, 
        reservation_date_end: date, client: str, room: Room, status: str) -> None:
        self.__reservation_date_start = reservation_date_start
        self.__reservation_date_end = reservation_date_end
        self.__client = client
        self.__room = room
        self.__status = status
        self.__consumption: list = []

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
    def room(self, room: Room) -> Room:
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

    def __dict__(self):
        return {'reservation_date_start': str(self.__reservation_date_start.strftime("%Y-%m-%d")), 'reservation_date_end': str(self.__reservation_date_end.strftime("%Y-%m-%d")), 'client': self.__client, 'room': dict(self.__room), 'status': self.__status, 'consumption': [dict(item) for item in self.__consumption]}

    def __repr__(self):
        return f"""Data de entrada : {self.__reservation_date_start.strftime("%Y-%m-%d")}, Data de saida : {self.__reservation_date_end.strftime("%Y-%m-%d")}, Cliente : {self.__client},Status : {self.__status}, Consumo : {self.__consumption}"""

    def __str__(self):
        return f"""Data de entrada : {self.__reservation_date_start.strftime("%Y-%m-%d")}, Data de saida : {self.__reservation_date_end.strftime("%Y-%m-%d")}, Cliente : {self.__client},Status : {self.__status}, Consumo : {self.__consumption}"""
    
    def __iter__(self):
        yield 'reservation_date_start', self.__reservation_date_start
        yield 'reservation_date_end', self.__reservation_date_end
        yield 'client', self.__client
        yield 'room', self.__room
        yield 'status', self.__status
        yield 'consumption', self.__consumption
    

    


