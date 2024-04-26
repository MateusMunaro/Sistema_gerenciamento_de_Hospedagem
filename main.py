from menu import Menu

def main():
    menu_list = [
        "___ Bem vindos a pousada ___",
        "Opções:",
        "1 - Consultar disponibilidade de um quarto.",
        "2 - Consultar reserva ja feita.",
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


if __name__ == "__main__":
    main()