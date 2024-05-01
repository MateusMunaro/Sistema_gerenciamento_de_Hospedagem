from datetime import date, datetime

from room import Room
from reservation import Reservation
from product import Product

class GuestHouse:

    DIARY_COST = 200.50
    
    def __init__(
            self, name: str = "", 
            contact: str = "", rooms: list[Room] = [],
            reservations: list[Reservation] = [], 
            products: list[Product] = []
        ) -> None:
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

    def __iter__(self):
        yield 'name', self.__name
        yield 'contact', self.__contact
        yield 'rooms', self.__rooms
        yield 'reservations', self.__reservations
        yield 'products', self.__products

    def upload_data(self):
        try:
            with open("guesthouse.txt", "r") as file:
                data = file.read()
                data = eval(data)
                self.__name = data["name"]
                self.__contact = data["contact"]
                self.__rooms = data["rooms"]
                self.__reservations = data["reservations"]
                self.__products = data["products"]
        except FileNotFoundError:
            print("Arquivo não encontrado.")
        print("Arquivo carregado com sucesso!")


    def save_data(self):
        with open("guesthouse.txt", "w") as file:
            data = dict(self)
            file.write(data)
        with open("products.txt", "w") as file:
            for product in self.__products:
                data = dict(product)
                file.write(data)
        with open("rooms.txt", "w") as file:
            for room in self.__rooms:
                data = dict(room)
                file.write(data)
        with open("reservations.txt", "w") as file:
            for reservation in self.__reservations:
                data = dict(reservation)
                file.write(data)

        print("Arquivo salvo com sucesso!")        
    
    def check_availability(self, start_date: date, end_date: date, room_number: int ) -> bool:
        is_free = True        
        for reservation in self.__reservations:
            if reservation.room.number != room_number and reservation.status != "I":
                if reservation.reservation_date_start != start_date and reservation.reservation_date_end != end_date:
                    return is_free
                else:
                    is_free = False
            else:
                is_free = False

        return is_free
                          
    
    def check_reservation(self, client_name: str):
        return [
            reservation for reservation in self.__reservations
            if reservation.client == client_name 
        ]
    
    def check_checkin(self, client_name: str):
        return [
            reservation for reservation in self.__reservations
            if reservation.client == client_name and reservation.status == "I"
        ]
                               

    def make_reservation(self, start_date: date, end_date: date, room_number: int, client_name: str):
        is_available = self.check_availability(start_date, end_date, room_number)
        if is_available:
            reservation = Reservation(start_date, end_date, client_name, room_number)
            self.__reservations.append(reservation)
            print("Reserva efetuada com sucesso!")
        else:
            print("Quarto não disponível!")


    def cancel_reservation(self, client_name: str):
        reservations = self.check_reservation(client_name)
        if len(reservations) != 0:
            for reservation in reservations:
                reservation.status = "C"
            print("Reserva cancelada com sucesso!")
        else:
            print("Nenhuma reserva encontrada!")

    def make_checkin(self, client_name: str):
        reservations = self.check_reservation(client_name)
        if len(reservations) != 0:
            for reservation in reservations:
                reservation.status = "I"
            print("Check-in efetuado com sucesso!")
        else:
            print("Nenhuma reserva encontrada!")

    def make_checkout(self, client_name: str):
        reservations = self.check_reservation(client_name)
        if len(reservations) != 0:
            for reservation in reservations:
                print(reservation)
                remain_days = reservation.reservation_date_end - reservation.reservation_date_start
                print("Dias restantes: ", remain_days.days)
                current_date = datetime.now().date()
                total_days = current_date - reservation.reservation_date_start
                print("Dias decorridos: ", total_days.days)
                total_costs = total_days.days * self.DIARY_COST + self.reservations.costs
                print("Custo total: ", total_costs)
                print("Custo por dia: ", self.DIARY_COST)
                print("Custo por dia em produtos: ", self.reservations.costs)

                reservation.status = "O"
            print("Check-out efetuado com sucesso!")
        else:
            print("Nenhuma reserva encontrada!")

    def register_consumption(self, client_name: str):
        reservation = self.check_checkin(client_name)[0]
        if len(reservation) != 0:
            print("Produtos disponíveis:")
            for product in self.__products:
                print(product)

            product_code = int(input("Código do produto: "))
            quantity = int(input("Quantidade: "))
            for product in self.__products:
                if product.code == product_code:
                    for i in range(quantity):
                        reservation.consumption.append(product)
            print("Consumo efetuado com sucesso!")
        else:
            print("Nenhuma reserva encontrada!")
        

            
        
