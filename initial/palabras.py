# modulo palabras
# desde aca administraremos la seleccion de palabras
# tambien el control sobre las letras elegidas
import diccionario as d

palabra_del_juego = ""

letras_usadas = []

largo_palabra = 0
# primer_letra = ''
# ------------------------------------------------
def resetLetrasUsadas():
    global letras_usadas
    letras_usadas = []


# ------------------------------------------------
def elegirpalabra():
    # 1-determinar cantidad palabras archivo
    # 2-elegir un numero random teniendo en cuenta la cantidad de palabras
    # 3-buscar en archivo la palabra y definir, cargar o asignarla a palabra_del_juego
    # -----------------------
    # 1- 2- por ahora voy a machear esta parte
    # 3
    global palabra_del_juego
    palabra_del_juego = list(d.recuperar_palabra())


# ------------------------------------------------
def mostrarpalabra():
    for letra in palabra_del_juego:
        if letra in letras_usadas:
            print(letra.upper(), end=" ")
        else:
            print(f"_", end=" ")
    print("\n")


# ------------------------------------------------
def mostrarresolucion():
    print(f"La palabra buscada era:\n")
    for letra in palabra_del_juego:
        print(letra.upper(), end=" ")
    print("\n")


# ------------------------------
def mostrarletrasusadas():
    print(f"Las letras usadas son:\n")
    count = 0
    for letra in letras_usadas:
        count += 1
        print(count, "-", letra.upper(), " | ", end=" ")
    print("\n")


# ------------------------------------------------
def puedo_formar_palabra():
    encontradas = 0
    largo_palabra = len(palabra_del_juego)
    for letra in letras_usadas:
        for i in range(largo_palabra):
            if letra == palabra_del_juego[i]:
                encontradas += 1
    if largo_palabra == encontradas:
        return True
    return False


# --------------------------------------------------
def agregar_letra(letra):
    global letras_usadas
    letras_usadas.append(letra)


# --------------------------------------------------
def esta_letra_en_palabra(letra):
    if letra in letras_usadas:
        return None
    else:
        if letra in palabra_del_juego:
            return True
    return False


# ------------------------------------------------
def acerto_palabra(palabra):
    return list(palabra.lower()) == palabra_del_juego


# elegirpalabra()
# mostrarpalabra()
# mostrarresolucion()
