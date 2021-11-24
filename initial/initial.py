from tkinter import *
from diccionario import *

mainWindow = Tk()
mainWindow.title("Ahorcado")
mainWindow.iconbitmap("../images/514163.ico")

csvFilePath = "../Diccionario.csv"
jsonFilePath = "../diccionario.json"

make_json(csvFilePath, jsonFilePath)

nameLabel = Label(mainWindow, text="Ingresar el nombre del jugador")
nameInput = Entry(mainWindow, width=50)
playButton = Button(
    mainWindow, text="Comenzar Juego", command=lambda: play(nameInput.get())
)


def play(player):
    return


nameLabel.grid(row=0, column=0, columnspan=3)
nameInput.grid(row=1, column=0, columnspan=3)
playButton.grid(row=2, column=0, columnspan=6)


mainWindow.mainloop()
