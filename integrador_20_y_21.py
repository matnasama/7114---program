## 🧠 Integradores

# ### Ejercicio 20 — Sistema de análisis de datos
# Desarrollar un programa que:
# 1. permita ingresar números hasta 0
def pedir_numeros():
    lista = []
    numeros = int(input("Ingresar un numero: "))
    while numeros >= 0:
        lista.append(numeros)
        numeros = int(input("Ingresar un numero: "))
    contador = len(lista)
    return lista, contador

# 2. los almacene en una lista
# - cantidad de datos
lista, contador = pedir_numeros()

# 3. luego calcule:
# - suma total
def sumar():
    suma = 0
    for i in lista:
        suma += i
    return suma
suma = sumar()

# - promedio
def promediar():
    promedio = suma/contador
    return promedio

# - cantidad de números pares
def contar_pares():
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    cantidad_pares = len(pares)
    return pares, cantidad_pares  

promedio = promediar()
pares, cantidad_pares = contar_pares()

# ### Ejercicio 21 — Persistencia de datos
# Extender el ejercicio anterior para:
# - guardar los datos en un archivo
# - luego leerlos desde el archivo
# - mostrar nuevamente los resultados
def mostrar_datos(suma, promedio, pares, cantidad_pares):
    print(f"la suma es {suma}")
    print(f"el promedio es {promedio}")
    print(f"los numeros pares son {pares} y la cantidad de numeros pares es {cantidad_pares}") 
    return (
        f"La suma es {suma}\n"
        f"El promedio es {promedio}\n"
        f"Los numeros pares son {pares}\n. La cantidad de numeros pares es {cantidad_pares}\n"     
    )


archivo = open("informe.txt", "w")
archivo.write(
    mostrar_datos(
        suma,
        promedio,
        pares,
        cantidad_pares
    )
)
archivo.close()
