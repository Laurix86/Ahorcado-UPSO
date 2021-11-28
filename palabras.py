#modulo palabras
#desde aca administraremos la seleccion de palabras
#tambien el control sobre las letras elegidas
import diccionario as d
import menuahorcado as m
palabra_del_juego = ''

letras_usadas = []

largo_palabra = 0
Texto1 = "Por favor, ingrese una letra y presione enter."
TextoSalir = "Pasar Finalizar presione (9):"
#primer_letra = ''
#------------------------------------------------
def ingresar_letra():
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    control = True
    texto = Texto1
    while control == True:
        m.textoSecundario(texto)
        m.textoSecundario(TextoSalir)
        valor_ingresado = input("\n>")
        x = str(valor_ingresado);
       
        #analizar el largo del ingreso x
        cantidad_letras_ingresadas = len(x)
        if(cantidad_letras_ingresadas == 0):
                 #print ("No se registro ningun ingreso. Recuerde que debe ingresar solo una letra y luego presionar enter")
                 control = False
                 break
        letra = x[0].lower()
        if letra == '9':
            return letra
        if(cantidad_letras_ingresadas == 1):
            if letra not in letras:                
                #print ("Debe ingresar solo una letra y luego presionar enter")
                control = False
                break  # Rompe directamente el bucle en cuanto encuentra un elemento que no es una letra
        else:
            #print("Usted ingreso mas de un caracter, vamos a utilizar el primer caracter ingresado, los otros seran descartados. Por favor, cuando se le solicite, trate de ingresar solo una letra y luego presionar enter.")
            if letra not in letras:
                #print (" El caracter ingresado, no es una letra.")
                control = False
                break  # Rompe directamente el bucle en cuanto encuentra un elemento que no es una letra
 
        if control == True:
            return letra
    return control
#------------------------------------------------
def largo_de_la_palabra():
    return len(palabra_del_juego)
#------------------------------------------------
def resetLetrasUsadas():
    global letras_usadas
    letras_usadas=[]
#------------------------------------------------
def elegirpalabra():
    #1-determinar cantidad palabras archivo    
    #2-elegir un numero random teniendo en cuenta la cantidad de palabras
    #3-buscar en archivo la palabra y definir, cargar o asignarla a palabra_del_juego
    #-----------------------
    #1- 2- por ahora voy a machear esta parte
    #3    
    global palabra_del_juego
    palabra_del_juego = list(d.recuperar_palabra())    
#------------------------------------------------
def mostrarpalabra():
    palabra_a_mostrar =''
    for letra in palabra_del_juego:
        if letra in letras_usadas:
            palabra_a_mostrar = palabra_a_mostrar + letra.upper() + " "
            #print(letra.upper(),end=" ")
        else:
            palabra_a_mostrar = palabra_a_mostrar + "_ "
            #print(f"_",end=" ")
    txt = m.Ancho_menu
    print(txt.format(palabra_a_mostrar)) 
    print("\n")    
#------------------------------------------------
def mostrarresolucion():    
    #print(f"La palabra buscada era:\n")
    palabra_a_mostrar =''
    for letra in palabra_del_juego:
        palabra_a_mostrar = palabra_a_mostrar + letra.upper() + " "
        #print(letra.upper(),end=" ")        
    txt = m.Ancho_menu
    print(txt.format(palabra_a_mostrar)) 
    print("\n")  
#------------------------------    
def mostrarletrasusadas():    
    #print(f"Las letras usadas son:\n")
    count = 0 
    for letra in letras_usadas:
        count +=1
        print(count,"-",letra.upper(),end=", ")        
    print("\n")
#------------------------------------------------    
def puedo_formar_palabra():
    encontradas = 0
    largo_palabra = len(palabra_del_juego)    
    for letra in letras_usadas:
        for i in range(largo_palabra):
            if letra == palabra_del_juego[i]:
                encontradas +=1
    if largo_palabra == encontradas:
        return True
    return False
#--------------------------------------------------    
def agregar_letra(letra):
    global letras_usadas
    letras_usadas.append(letra)    
#-------------------------------------------------- 
def esta_letra_en_palabra(letra):
    if letra in letras_usadas:
        return None
    else:
        if letra in palabra_del_juego:
            return True
    return False
#------------------------------------------------   
def acerto_palabra(palabra):
    return list(palabra.lower()) ==  palabra_del_juego
# elegirpalabra()
# mostrarpalabra()
# mostrarresolucion()
