from menu import Menu
from guesthouse import GuestHouse

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

    while True:

        main_menu = Menu(menu_list)
        opt = main_menu.run()
        guesthouse = GuestHouse()
        guesthouse.upload_data()


        if opt == 1:
            print("Consultar disponibilidade de um quarto.")
            number = int(input("Número do quarto: "))
            start_date = int(input("Data de entrada: ")) 
            end_date = int(input("Data de saída: "))             
            is_availble = guesthouse.check_availability(number, start_date, end_date)
            print("Quanto disponivel!" if is_availble else "Quarto não disponível!")
        elif opt == 2:
            print("Consultar reserva ja feita.")
        elif opt == 3:
            print("Realizar uma reserva.")
        elif opt == 4:
            print("Cancelar reserva.")
        elif opt == 5:
            print("Realizar check-in.")
        elif opt == 6:
            print("Realiza check-out.")
        elif opt == 7:
            print("Registrar consumo.")
        elif opt == 8:
            print("Salvar.")
            guesthouse.save_data()
        elif opt == 0:
            print("Saindo...")
            quit()

        


if __name__ == "__main__":
    main()
