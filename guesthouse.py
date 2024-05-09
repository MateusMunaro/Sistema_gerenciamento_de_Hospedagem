import json

from typing import List
from datetime import date, datetime

from room import Room
from reservation import Reservation
from product import Product

class GuestHouse:

    DIARY_COST = 10.4
    
    def __init__(
            self, name: str, 
            contact: str, 
            room: List[Room],
            reservations: List[Reservation], 
            products: List[Product]
        ) -> None:
        self.__name = name
        self.__contact = contact
        self.__rooms = room
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

    def __dict__(self):
        return {
            "name": self.__name,
            "contact": self.__contact,
            "rooms": [room.__dict__() for room in self.__rooms],
            "reservations": [reservation.__dict__() for reservation in self.__reservations],
            "products": [product.__dict__() for product in self.__products]
        }

    #carrega informações do Json
    def upload_data(self):
        try:
            with open("guesthouse.json", "r") as file:
                print("Carregando arquivo...")
            
                data = json.loads(str(file.read()))
                self.__name = data['name']
                self.__contact = data['contact']
                self.__rooms = [Room(**room) for room in data['rooms']]
                self.__reservations = [
                    Reservation(
                        reservation_date_start=datetime.strptime(reservation['reservation_date_start'], "%Y-%m-%d").date(),
                        reservation_date_end=datetime.strptime(reservation['reservation_date_end'], "%Y-%m-%d").date(), 
                        client=reservation['client'],
                        room=Room(**reservation['room']), 
                        status=reservation['status']
                    ) 
                    for reservation in data['reservations']  
                ]
                self.__products = [Product(**product) for product in data['products']]
                print("Arquivo carregado com sucesso!")
                    
               
        except FileNotFoundError:
            print("Arquivo não encontrado.")

    #salva os dados em um arquivo tipo Json
    def save_data(self):
        with open("guesthouse.json", "w") as file:
            data = self.__dict__()
            data = json.dump(data, file)    
        print("Arquivo salvo com sucesso!")        
    
    def check_availability(self, start_date: date, end_date: date, room_number: int) -> bool:
        for reservation in self.__reservations:
            if reservation.room.number != room_number:
                if reservation.status != "I" or reservation.status != "C":
                    if reservation.reservation_date_start != start_date and reservation.reservation_date_end != end_date:
                        return is_free
                    else:
                        is_free = False
                else:
                    is_free = False
            else:
                continue

        return is_free
                          
    #faz a verificação se existe uma reserva em um nome
    def check_reservation(self, client_name: str):
        return [
            reservation for reservation in self.__reservations
            if reservation.client == client_name 
        ]
    #verifica se esse nome ja fez checkin
    def check_checkin(self, client_name: str):
        return [
            reservation for reservation in self.__reservations
            if reservation.client == client_name and reservation.status == "I"
        ]

    #faz a busca para ver se o quarto esta vago
    def find_room(self, room_number: int):
        for room in self.__rooms:
            if room.number == room_number:
                return room                   
    #faz a reserva e adiciona dentro da lista de reservas
    def make_reservation(self, start_date: date, end_date: date, room_number: int, client_name: str):
        is_available = self.check_availability(start_date, end_date, room_number)
        if is_available:
            room = self.find_room(room_number)
            current_reservation = Reservation(start_date, end_date, client_name, room, "A")
            self.__reservations.append(current_reservation)
            print("Reserva efetuada com sucesso!")
        else:
            print("Quarto não disponível!")

    #cancela a reserva feita
    def cancel_reservation(self, client_name: str):
        reservations = self.check_reservation(client_name)
        if len(reservations) != 0:
            for reservation in reservations:
                reservation.status = "C"
            print("Reserva cancelada com sucesso!")
        else:
            print("Nenhuma reserva encontrada!")
    #efetua o check-in mudando o status da reserva
    def make_checkin(self, client_name: str):
        reservations = self.check_reservation(client_name)
        if len(reservations) != 0:
            for reservation in reservations:
                reservation.status = "I"
            print("Check-in efetuado com sucesso!")
        else:
            print("Nenhuma reserva encontrada!")

    #efetua o check-out mostrando todas as informações
    def make_checkout(self, client_name: str):
        reservations = self.check_reservation(client_name)
        if len(reservations) != 0:
            for reservation in reservations:
                print(reservation)
                remain_days = reservation.reservation_date_end - reservation.reservation_date_start
                print("Dias restantes: ", remain_days.days)
                current_date = datetime.now().date()
                total_days = current_date
                print("Dias decorridos: ", total_days.day)
                total_costs = total_days.day * reservation.room.daily + reservation.costs + self.DIARY_COST if total_days.day != 0 else + self.DIARY_COST * reservation.room.daily + 200
                print("Custo total: ", total_costs)
                print("Custo por dia: ", reservation.room.daily * total_days.day)
                print("Custo por dia em produtos: ", reservation.costs)

                reservation.status = "O"
            print("Check-out efetuado com sucesso!")
        else:
            print("Nenhuma reserva encontrada!")
    #faz a validação do consumo
    def register_consumption(self, client_name: str):
        reservation = self.check_checkin(client_name)
        if len(reservation) != 0:
            print("Produtos disponíveis:")
            for product in self.__products:
                print(product)

            product_code = int(input("Código do produto: "))
            quantity = int(input("Quantidade: "))
            for product in self.__products:
                if product.code == product_code:
                    for i in range(quantity):
                        reservation[0].consumption.append(product)
            print("Consumo efetuado com sucesso!")
        else:
            print("Nenhuma reserva encontrada!")
        

            
        
