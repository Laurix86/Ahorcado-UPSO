import os
from tkinter import *


def menuInicial(mainWindow):
    global menu
    menu = IntVar()

    def showChange():
        if menu.get() == 1:
            nameLabel.grid(row=4, column=1, columnspan=3)
            nameInput.grid(row=5, column=1, columnspan=2)
            playButton.grid(row=6, column=2, columnspan=2)
        else:
            nameLabel.grid_forget()
            nameInput.grid_forget()
            playButton.grid_forget()

    Radiobutton(
        mainWindow,
        text="Nuevo Juego",
        variable=menu,
        value=1,
        command=showChange,
        state=NORMAL,
    ).grid(row=0, column=0, columnspan=6)
    Radiobutton(
        mainWindow, text="Ultima Partida", variable=menu, value=2, command=showChange
    ).grid(row=1, column=0, columnspan=6)
    Radiobutton(
        mainWindow, text="Agregar Palabras", variable=menu, value=3, command=showChange
    ).grid(row=2, column=0, columnspan=6)
    Radiobutton(
        mainWindow,
        text="Ver tabla posiciones",
        variable=menu,
        value=4,
        command=showChange,
    ).grid(row=3, column=0, columnspan=6)

    nameLabel = Label(mainWindow, text="Ingresar el nombre del jugador")
    nameInput = Entry(mainWindow, width=30)
    playButton = Button(
        mainWindow, text="Comenzar Juego", command=lambda: play(nameInput.get())
    )

    Button(mainWindow, text="Salir").grid(row=6, column=5, columnspan=2)

    # frame.grid(row=0, column=0, columnspan=3)


# '1':'Nuevo Juego', '2':'Ultima Partida','3':'Agregar Palabras','4':'Ver tabla posiciones','9':'Salir'
def play(player):
    return
