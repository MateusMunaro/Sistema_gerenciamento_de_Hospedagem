from Room import Room
from Reservation import Reservation
from Product import Product

class GuestHouse:
    def __init__(self, name: str, contact: str, rooms: Room, reservations: Reservation, products: Product):
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
    def contact(self, contact: str):
        self.__contact = contact

    @property
    def rooms(self):
        return self.__rooms
    
    @rooms.setter
    def rooms(self, rooms: list):
        self.__rooms = rooms

    @property
    def reservations(self):
        return self.__reservations
    
    @reservations.setter
    def reservations(self, reservations: list):
        self.__reservations = reservations

    @property
    def products(self):
        return self.__products
    
    @products.setter
    def products(self, products: list):
        self.__products = products

    def upload_data(self):
        pass

    def save_data(self):
        pass
    
    def check_availability(self, number: int, start_day: int, end_day: int) -> bool:
        for reservation in self.__reservations:
            if reservation.number == number:
                if not (end_day <= reservation.start_day or start_day >= reservation.end_day):
                    return False
        return True
    
    def check_reservation(self, reservation: Reservation):
        pass

    def make_reservation(self, reservation: Reservation):
        if self.check_availability(reservation.number, reservation.start_day, reservation.start_day):
            self.__reservations.append(reservation)
            print("Reservation made successfully.")
        else:
            print("Room is not available for the selected dates.")

    def cancel_reservation(self, reservation: Reservation):
        pass

    def make_checkin(self, reservation: Reservation):
        pass

    def make_checkout(self, reservation: Reservation):
        pass
