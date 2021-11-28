import menuahorcado as m #desde aca modemos administrar interface del menu
import leerletra as l #desde aca podemos utilizar para solicitar lectura de una letra para una palabra
import imprimirahorcado as i #graficar el estado del juego, grafica el muñeco
#import palabras as p
import jugar as j
#----------------------------
#variables de configuracion
cantidad_jugadores = 1
nombre1 = 'Player1'
#jugar = False
estado = ''
#----------------------------
def quiere_seguir_jugando():    
    while True:
        print("Quiere volver a JUGAR\nIngrse\n1- Sigo Jugando\n2-Salir\n")
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
        print("Que lastima chango\n")
    
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

