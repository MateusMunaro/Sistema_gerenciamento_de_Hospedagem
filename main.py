import os

from datetime import datetime

from menu import Menu
from guesthouse import GuestHouse
from room import Room
from product import Product
from reservation import Reservation

def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def main():
    menu_list = [
        "___ Bem vindos a pousada ___",
        "Opções:",
        "1 - Consultar disponibilidade de um quarto.",
        "2 - Consultar reserva já feita.",
        "3 - Realizar uma reserva.",
        "4 - Cancelar reserva.",
        "5 - Realizar check-in.",
        "6 - Realiza check-out.",
        "7 - Registrar consumo.",
        "8 - Salvar.",
        "0 - Sair"
    ]

    main_room = Room(1, "Simples", 100, [])
    suite_room = Room(2, "Suite", 200, [])
    delux_room = Room(3, "Luxo", 300, [])

    coca_cola = Product(1, "Coca-cola", 5)
    fanta = Product(2, "Fanta", 5)
    guarana = Product(3, "Guarana", 5)
    french_fries = Product(4, "French Fries", 20)
    meat = Product(5, "Meat", 50)
    chocolate = Product(6, "Chocolate", 10)
    water = Product(7, "Water", 10)

    boss_reservation = Reservation( 
        datetime.strptime("2022-01-01", "%Y-%m-%d"), 
        datetime.strptime("2022-01-02", "%Y-%m-%d"),
        "Boss", main_room, "O"
    )


    guesthouse = GuestHouse(
        name="Pousada Top",
        contact="123456789",
        room=[ main_room, suite_room, delux_room ],
        reservations=[boss_reservation],
        products=[
            coca_cola, fanta, guarana, french_fries, meat, chocolate, water
        ]
    )
    guesthouse.upload_data()

    while True:

        main_menu = Menu(menu_list)
        opt = main_menu.run()

        if opt == 1:
            number = int(input("Número do quarto: "))
            start_date = input("Data de entrada (aaaa-mm-dd): ") 
            end_date = input("Data de saída (aaaa-mm-dd): ")             
            is_availble = guesthouse.check_availability(number, start_date, end_date)
            print("Quanto disponivel!" if is_availble else "Quarto não disponível!")
        elif opt == 2:
            client = input("Nome do cliente: ")
            data = guesthouse.check_reservation(client)
            print("Nenhuma reserva feita" if data == [] else data)

        elif opt == 3:
            start_date = input("Data de entrada (aaaa-mm-dd): ")
            end_date = input("Data de saida: (aaaa-mm-dd): ")
            number = int(input("Numero do quarto: "))
            client = input("Nome do cliente: ")
            start_date = datetime.strptime(str(start_date), "%Y-%m-%d").date()
            end_date = datetime.strptime(str(end_date), "%Y-%m-%d").date()
            guesthouse.make_reservation(start_date, end_date, number, client)

        elif opt == 4:
            client = input("Nome do cliente: ")
            data = guesthouse.cancel_reservation(client)
            print(data)
        elif opt == 5:
            client = input("Nome do cliente: ")
            guesthouse.make_checkin(client)
        elif opt == 6:
            client = input("Nome do cliente: ")
            guesthouse.make_checkout(client)
        elif opt == 7:
            print("Registrar consumo.")
            client = input("Nome do cliente: ")
            guesthouse.register_consumption(client)
        elif opt == 8:
            guesthouse.save_data()
        elif opt == 0:
            print("Saindo...")
            quit()



        


if __name__ == "__main__":
    main()
