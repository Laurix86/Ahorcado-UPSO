import os
from tkinter import *
from diccionario import *
import random
import initialWindow

# Creación Diccionario en archivo JSON
csvFilePath = "../Diccionario.csv"
jsonFilePath = "../diccionario.json"
make_json(csvFilePath, jsonFilePath)

# Selección palabra para jugar

numberWord = str(random.randint(0, 5000))
with open(jsonFilePath, "r", encoding="UTF-8") as diccionario:
    data = json.load(diccionario)
    selectedWord = data[numberWord]
    # print("palabra: ", selectedWord)

mainWindow = Tk()
mainWindow.title("Ahorcado")
mainWindow.iconbitmap("../images/514163.ico")

nameLabel = Label(mainWindow, text="Ingresar el nombre del jugador")
nameInput = Entry(mainWindow, width=50)
playButton = Button(
    mainWindow, text="Comenzar Juego", command=lambda: play(nameInput.get())
)


def play(player):
    return


initialWindow.menuInicial(mainWindow)
# primerMenu.grid(row=0, column=0, columnspan=3)
# nameLabel.grid(row=1, column=0, columnspan=3)
# nameInput.grid(row=2, column=0, columnspan=3)
# playButton.grid(row=3, column=0, columnspan=6)
playButton.pack()


mainWindow.mainloop()
