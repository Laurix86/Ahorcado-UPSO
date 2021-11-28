import os

clearConsole = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")
menu = {
    "0": {
        "1": "Nuevo Juego",
        "2": "Ultima Partida",
        "3": "Agregar Palabras",
        "4": "Ver tabla posiciones",
        "9": "Salir",
    },
    "01": {"1": "1 vs CPU", "2": "2 vs CPU", "3": "1 vs 1", "9": "Menu Anterior"},
    "02": {"1": "Seguir Jugando", "9": "Menu Anterior"},
    "03": {"1": "Buscar Archivo", "9": "Menu Anterior"},
    "04": {"1": "Reset Posiciones", "9": "Menu Anterior"},
    "011": {"1": "Jugar", "9": "Menu Anterior"},
}
# menuprincipal = {'1':'Nuevo Juego', '2':'Ultima Partida','3':'Agregar Palabras','4':'Ver tabla posiciones','9':'Salir'}
# menu1 = {'1':'1 vs CPU', '2':'2 vs CPU','3':'1 vs 1','9':'Menu Anterior'}
# menu2 = {'1':'Seguir Jugando', '9':'Menu Anterior'}
# menu3 = {'1':'Buscar Archivo', '9':'Menu Anterior'}
# menu4 = {'1':'Reset Posiciones', '9':'Menu Anterior'}
# menu9 = {'9':'Volver/Salir'}
opcionmenu = "0"
menuactivo = menu[opcionmenu]
opcion = "0"


def mostrarmenu():
    clearConsole()
    print(f"Menu:", opcionmenu, "\n")
    for op in menuactivo:
        print(f"", op, "-", menuactivo[op], "       ")
    print(f"---------------------------------\n")


# ------------------------------------------ fin mostrar menu
def leeropcion():
    control = True
    while control == True:

        valor_ingresado = input("Por favor, ingrese una opcion:>\n")
        largo_cadena_ingresadas = len(valor_ingresado)
        if largo_cadena_ingresadas == 0:
            print(
                "No se registro ningun ingreso. Recuerde que debe ingresar algunas de las opciones del menu y presionar enter.\n"
            )
            control = False
            break
        digito = valor_ingresado[0]
        if largo_cadena_ingresadas == 1:
            if digito not in menuactivo:
                print(
                    "Debe ingresar algunas de las opciones del menu y presionar enter.\n"
                )
                control = False
                break  # Rompe directamente el bucle en cuanto encuentra un elemento que no es una letra
        else:
            print(
                "Usted ingreso mas de un caracter, vamos a utilizar el primer caracter ingresado, los otros seran descartados.\n Por favor, cuando se le solicite, trate de ingresar algunas de las opciones del menu y presionar enter.\n"
            )
            if digito not in menuactivo:
                print(" El caracter ingresado, no es una opcion del menu.")
                control = False
                break  # Rompe directamente el bucle en cuanto encuentra un elemento que no es una opcion

        if control == True:
            return digito
    return control


# ------------------------------------------ fin leeropcion
def cambiardemenu(opcion):
    global menu
    global menuactivo
    global opcionmenu
    estado = ""
    profundidadmenu = len(opcionmenu)
    # lo uso para determinar donde estoy del menu siendo 0 el primer nivel,

    # controlo si estoy en un nivel de definicion de accion y la opcion elegida es accion, entonces cambio el estado,
    # sino navego el menu.
    if profundidadmenu == 3 and opcion != "9":
        estado = menuactivo[opcion]
        print(f"estado actual", estado)
    else:
        # navegando el menu
        if opcion == "9":
            # si opcion es 9 entonces debo salir o volver
            if profundidadmenu > 1:
                # entonces tengo q volver al menu anterior
                opcionmenu = opcionmenu[0 : profundidadmenu - 1]
                menuactivo = menu[opcionmenu]

            else:
                opcionmenu = "Salir"
        elif profundidadmenu < 4 and opcion in menuactivo:
            print(f"la opcion:", opcion, "opcionmenu", opcionmenu)
            if opcion != "9":
                opcionmenu = opcionmenu + opcion
                menuactivo = menu[opcionmenu]
                print(f"Nueva opcion:", opcionmenu)
                # *****************
            else:
                print(f"invalida:", opcion)
        else:
            print(f"Opcion invalida:", opcion)

    return estado


# ------------------------------------------ fin cambiardemenu
def cerrar():
    # clearConsole()
    print(f"Saliendo\nGracias x jugar. Nos vemos Pronto.")
