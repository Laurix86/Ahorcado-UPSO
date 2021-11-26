import os
from tkinter import *
from diccionario import *
import random
import initialWindow
import imprimirDibujo


# Creación Diccionario en archivo JSON
csvFilePath = "../Diccionario.csv"
jsonFilePath = "../diccionario.json"
# make_json(csvFilePath, jsonFilePath)

# Selección palabra para jugar

numberWord = str(random.randint(0, 5000))
with open(jsonFilePath, "r", encoding="UTF-8") as diccionario:
    data = json.load(diccionario)
    selectedWord = data[numberWord]
    # print("palabra: ", selectedWord)

mainWindow = Tk()
mainWindow.geometry("1400x600")
mainWindow.title("Ahorcado")
mainWindow.iconbitmap("../images/514163.ico")

frameMenu = Frame(mainWindow)
frameMunieco = Frame(mainWindow)

# menuBar = Menu(mainWindow)
# opcionesMenu= Menu(menuBar, tearoff=0)
# opcionesMenu.add


initialWindow.menuInicial(frameMenu)
imprimirDibujo.imprimirparte(5, frameMunieco)
# frameMenu.pack()
frameMenu.grid(row=0, column=0, columnspan=5)
frameMunieco.grid(row=0, column=5, columnspan=5)

# playButton.pack()


mainWindow.mainloop()
