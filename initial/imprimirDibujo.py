# errores = 1
from tkinter import *


def imprimirparte(errores, window):
    # uso dibujo para agregar lo que voy a dibujar. luego lo voy a recorrer y voy a ir dibujando
    dibujo = []
    pedacitos = ""
    tituloLabel = Label(window, text="Bienvenidos\nal juego\ndel Ahorcado")
    tituloLabel.grid(row=0, column=2, columnspan=6)
    # c
    Cabeza = [114, 115, 116, 134, 138, 155, 159, 176, 180, 198, 199, 200]
    Tronco = [220, 241, 262, 283, 304, 325, 346]
    BIzq = [258, 259, 260, 261]
    BDer = [263, 264, 265, 266]
    PIzq = [366, 386, 406, 426]
    PDer = [368, 390, 412, 434]
    # horca = [menores que 11 o multiplo de 21 o mayores que 525]
    vertical = [
        21,
        42,
        63,
        84,
        105,
        126,
        147,
        147,
        168,
        189,
        210,
        231,
        252,
        273,
        294,
        315,
        336,
        357,
        378,
        399,
        420,
        441,
        462,
        483,
        504,
        525,
    ]

    cuerda = [31, 52, 73, 94]
    ojos = [135, 137]
    dibujo.append(Cabeza)
    dibujo.append(Tronco)
    dibujo.append(BIzq)
    dibujo.append(BDer)
    dibujo.append(PDer)
    dibujo.append(PIzq)
    imprimirblanco = False
    contadorsaltos = 0

    for i in range(0, 545):
        dibuLabel = Label(window, text=pedacitos)
        if i <= 10 or i > 525:
            pedacitos = pedacitos + "-"
            # pedacitos = "primero"
            # print("-", end="")
        else:
            if i in vertical:
                contadorsaltos += 1
                pedacitos = pedacitos + "" + "\n"
                pedacitos = pedacitos + "|" + ""
                # pedacitos = "segundo"
                contadorsaltos += 1
            else:
                imprimirblanco = True
                # busco i en dibujo
                for e in range(errores):
                    if i in dibujo[e]:
                        pedacitos = pedacitos + "*" + ""
                        # pedacitos = "tercero"
                        imprimirblanco = False
                if imprimirblanco:
                    # pedacitos = "cuarto"
                    pedacitos = pedacitos + " " + ""
    dibuLabel.grid(row=0, column=6)


""" 
print(f"La palabra es:")
print(f" _ _ _ _ _ _")
print()
print(f"usted a cometido", errores, "errores")
imprimirparte()
print()
print(f"por favor ingrese una letra nueva:") """
