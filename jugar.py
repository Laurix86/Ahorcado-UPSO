#jugar
#1- Elegir palabra (vs pc, elige pc)
#2- Mostrar Palabra
#3- Leer Letra
#4-1 Si es letra entonces ver si esta en palabra
#4-2 Si es numero dar opcion de salir

#4-1-1 Esta en palabra - actualizar letras ingresadas
#						- 
import palabras as pl
#import leerletra as ll
import imprimirahorcado as ia
import menuahorcado as m
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')



VIDAS = 6
letra = False
errores = 0
#pl.letras_usadas
#tine vidas? ya perdio
#ya gano? quiere arriesgar?
#quiere Salir? quiere seguir jugando?
def reset():
    global errores,letra    
    errores = 0
    letra = False
    pl.resetLetrasUsadas()

#-----------------------
def tiene_vidas():
    
    if (VIDAS - errores) > 0:
        return True
    return False
#-----------------------
def gano():
    if pl.puedo_formar_palabra():
        return True
    return False    
#-----------------------    
def pedir_ingresar_letra():
    global letra
    letra = False
    while letra == False:
        letra = pl.ingresar_letra()
#-----------------------
#def quiere_arriesgar():    
#    while True:
#        print("\n")
#        print("***********************************************************************\n")
#        print("***********************************************************************\n")
#        print("***********************************************************************\n")
#        print("***********************************************************************\n")
#        respuesta = input("-->")
#        if respuesta == '1':
#            return True
#        elif respuesta == '2':
#            return False
#-----------------------
def arriesgar(titulo):
    titulo_encabezado = titulo
    m.encabezado(titulo_encabezado)
    palabraArriesgada = input("Arriesga chango:\n>")
    if pl.acerto_palabra(palabraArriesgada):
        return 'Gano'
    else:
        return 'Perdio'
#-----------------------

def printjuego():
    clearConsole()
    x = str(pl.largo_de_la_palabra())
    titulo_encabezado = f"Palabra buscada, tiene "+x+" letras"
    m.encabezado(titulo_encabezado)
    pl.mostrarpalabra()
    titulo_secundario = f"Las letras usadas son"
    m.encabezado(titulo_secundario)
    pl.mostrarletrasusadas()        
    ia.imprimirparte(errores)

def jugar():
    reset()
    pl.elegirpalabra()
    #pl.mostrarresolucion()
    #x = input("la palabra mostrada\n")
    #-------------------------
    
    #-------------------------
    global letra
    global errores
    seguir = tiene_vidas()
    while seguir: #and quiere arrisgar # and sigue_jugando            
        #----        
        printjuego()
        pedir_ingresar_letra()
        if letra == '9':
            return 'Salir'#si 9 terminar ya llegara
        esta_letra_en_palabra = pl.esta_letra_en_palabra(letra)#si esta devuelve true        
        if esta_letra_en_palabra:                       
            pl.agregar_letra(letra)
            printjuego()        
            if gano():
                return 'Gano'
            if m.quiere_arriesgar():
                return arriesgar("Suerte!!!")
        elif esta_letra_en_palabra == False:
            pl.agregar_letra(letra)
            errores +=1
            seguir = tiene_vidas()
            if not seguir:
                printjuego()
                return arriesgar(f"última oportunidad, Debe arriesgar")

        

    