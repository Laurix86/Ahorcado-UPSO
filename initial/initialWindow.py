import os
from tkinter import *


def menuInicial(inWindow):

    global menu
    menu = IntVar()

    Radiobutton(inWindow, text="Nuevo Juego", variable=menu, value=1).pack()
    Radiobutton(inWindow, text="Ultima Partida", variable=menu, value=2).pack()
    Radiobutton(inWindow, text="Agregar Palabras", variable=menu, value=3).pack()
    Radiobutton(inWindow, text="Ver tabla posiciones", variable=menu, value=4).pack()
    Radiobutton(inWindow, text="Salir", variable=menu, value=9).pack()


# '1':'Nuevo Juego', '2':'Ultima Partida','3':'Agregar Palabras','4':'Ver tabla posiciones','9':'Salir'
