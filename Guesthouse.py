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

        @property
        def name(self):
            return self.__name
        
        @name.setter
        def name(self, name: str):
            self.__name = name

        @property
        def contact(self):
            return self.__contact
        
        @contact.setter
        def contact(self, contact: int):
            self.__contact = contact

        @property
        def rooms(self):
            return self.__rooms
        
        @rooms.setter
        def rooms(self, rooms: Room):
            self.__rooms = rooms

        @property
        def reservations(self):
            return self.__reservations
        
        @reservations.setter
        def reservations(self, reservations: Reservation):
            self.__reservations = reservations

        @property
        def products(self):
            return self.__products
        
        @products.setter
        def products(self, products: Product):
            self.__products = products

        

        