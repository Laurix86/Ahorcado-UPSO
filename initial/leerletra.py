#def leerletra():
 # entrada = input("por favor ingrese una letra:")
    #si es letra ver si esta ingresada previamente llamar a versiestaenlista
    #sino volver a pedir ingresar letra *volver a leerletra
    #cuando sea letra ver 
    #si ésta fue ingresada previamente
    #si fue entonces *volver a leerletra
    #si no fue ingresada en forma previa, entonces ver si esta en palabra
    #si esta en palabra asignar a palabra
    #si no esta aumentar 1 error
    
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#valoringresado = input("Hello world:\n")
#print(f'acabas de ingresar {valoringresado}')
# -*- coding: utf-8 -*-
def letra():
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    control = True
    while control == True:
        valor_ingresado = input("Por favor, ingrese una letra y presione enter:>\n")
        x = str(valor_ingresado);
       
        #analizar el largo del ingreso x
        cantidad_letras_ingresadas = len(x)
        if(cantidad_letras_ingresadas == 0):
                 print ("No se registro ningun ingreso. Recuerde que debe ingresar solo una letra y luego presionar enter")
                 break
        letra = x[0]
        if(cantidad_letras_ingresadas == 1):
            if letra not in letras:
                    print ("Debe ingresar solo una letra y luego presionar enter")
                    control = False
                    break  # Rompe directamente el bucle en cuanto encuentra un elemento que no es una letra
        else:
            print("Usted ingreso mas de un caracter, vamos a utilizar el primer caracter ingresado, los otros seran descartados. Por favor, cuando se le solicite, trate de ingresar solo una letra y luego presionar enter.")
            if letra not in letras:
                print (" El caracter ingresado, no es una letra.")
                control = False
                break  # Rompe directamente el bucle en cuanto encuentra un elemento que no es una letra
 
        if control == True:
            return letra
    return control
valor = letra()
print(valor)
