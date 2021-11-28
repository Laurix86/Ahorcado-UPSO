import menuahorcado as m #desde aca modemos administrar interface del menu
import palabras as pl
#desde aca podemos utilizar para solicitar lectura de una letra para una palabra
import imprimirahorcado as i #graficar el estado del juego, grafica el muñeco
import jugar as j
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
#----------------------------
#variables de configuracion
cantidad_jugadores = 1
nombre1 = 'Player1'
#jugar = False
estado = ''
#----------------------------
def quiere_seguir_jugando():    
    while True:
        titulo_encabezado = f"Quiere volver a JUGAR"
        m.encabezado(titulo_encabezado)

        #print("Quiere volver a JUGAR\nIngrse\n1- Sigo Jugando\n2-Salir\n")
        m.elegirOpcion("Ingrese","Sigo Jugando","Salir")
        respuesta = input("-->")
        if respuesta == '1':
            return 'Jugar'
        elif respuesta == '2':
            return 'Salir'

#voy a hacer un ciclado hasta que la opcion elegida sea salir
#primero mostrar menu    
#leer opcion ingresada
#cambiardemenu
while estado != 'Salir':
    if estado == 'Gano':
        print("Felicitaciones chango\n")
        
    if estado == 'Perdio':
        clearConsole()
        titulo_encabezado = f"Que lastima chango"
        m.encabezado(titulo_encabezado)
        titulo_secundario = f"La palabra era"
        m.textoSecundario(titulo_secundario)               
        pl.mostrarresolucion()
    
    if estado in ['Gano','Perdio']:
        estado = quiere_seguir_jugando()
    else:
        m.mostrarmenu()
        m.opcion = m.leeropcion()
        estado = m.cambiardemenu(m.opcion)
    
    if estado == 'Jugar':        
        estado = j.jugar()        
    
    

        
#if estado == 'Salir':
m.cerrar()

