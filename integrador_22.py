# ### Ejercicio 22 — Sistema completo

# Simular un sistema que:

# 1. permita ingresar datos numéricos
# 2. los almacene en una estructura
# 3. los procese
# 
#  4. los persista en archivo
# El programa debe mostrar:

# - valores mayores a un umbral (ej: >10)
# - promedio
# - valor máximo
def ingresar_numeros():
    matriz = []
    contador = 0
    mayores_25 = []
    print("Para finalizar el programa ingresar un numero NEGATIVO")
    numeros = int(input("Ingresar un numero: "))
    while numeros >= 0:
        matriz.append(numeros)
        numeros = int(input("Ingresar un numero: "))
    contador = len(matriz)
    mayor = max(matriz)
    for numeros in matriz:
        if numeros > 25:
            mayores_25.append(numeros)
    return matriz, contador, mayor, mayores_25

matriz, contador, mayor, mayores_25 = ingresar_numeros()

def mostrar_datos(matriz, contador, mayor, mayores_25):
    return(
        f"La lista de valores ingresados es: {matriz}\n"
        f"La cantidad de datos ingresados es: {contador}\n"
        f"El numero mas grande es: {mayor}\n"
        f"Los numeros mayores a 25 son: {mayores_25}"
    )

archivo = open("sistema.txt", "w")
archivo.write(
    mostrar_datos(
        matriz,
        contador,
        mayor,
        mayores_25
    )
)
archivo.close()