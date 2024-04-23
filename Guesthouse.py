import Room
import Reservation
import Product

class GuestHouse:
    def __init__(self, name: str, contact: int, rooms: Room, reservations: Reservation, products: Product):
        self.__name = name 
        self.__contact = contact
        self.__rooms = rooms
        self.__reservations = reservations
        self.__products = products

        