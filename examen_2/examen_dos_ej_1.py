# Escribí un programa que pida al usuario palabras hasta que ingrese la palabra 'fin'. Al finalizar, mostrá cuántas palabras ingresó y cuál tiene más letras.
# El programa debe organizarse con las siguientes funciones:
# pedir_palabras()  → pide palabras al usuario hasta que ingrese 'fin' y las devuelve en una lista.
# analizar(palabras)  → recibe la lista y devuelve la cantidad y la palabra más larga.
# mostrar_resultados(cantidad, mas_larga)  → muestra los resultados por pantalla.

# definiendo variables

palabras = []
cantidad = []

# definiendo funciones

def pedir_palabras():
    palabras = []
    palabra = input("Ingresa una palabra (Para finalizar ingresa la palabra FIN): ")
    while palabra.lower() != "fin":
        palabras.append(palabra)
        palabra = input("Ingresa una palabra (Para finalizar ingresa la palabra FIN): ")
    return palabras

def analizar(palabras):
    if not palabras:
        return 0, None
    cantidad = len(palabras)
    mas_larga = max(palabras, key=len)
    return cantidad, mas_larga    

palabras = pedir_palabras()
cantidad, mas_larga = analizar(palabras)

def mostrar_resultados(palabras, cantidad, mas_larga):
    print(f"La las palabras de la lista son: {palabras}")
    print(f"La cantidad de palabras es:  {cantidad}")
    print(f"La palabra mas larga es:  {mas_larga}")

mostrar_resultados(palabras, cantidad, mas_larga)
