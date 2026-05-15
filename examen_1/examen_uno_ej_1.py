
# # Ejercicio 1 — Estructuras de control 
# # programa para pedir numeros enteros hasta que sea un numero negativo
# # mostrar cuantos numeros ingresaron
# # mostrar cual es el mayor numero ingresado
# # 
# numeros = []

# # funciones

# def pedir_numeros(numeros):
# # pide numeros y los devuelve en una lista
#     numero = int(input("Ingrese un numero entero(negativo para terminar programa): "))
#     while numero > 0:
#         numeros.append(numero)
#         numero = int(input("Ingrese un numero entero(negativo para terminar programa): "))
#     return numeros


# def analizar(numeros):
#     cantidad = 0
#     mayor = 0
#     for i in numeros:
#         # suma al contador la cantidad de numeros ingresados 
#         cantidad +=1  
#         # esto es igual a cantidad = cantidad + 1
#         #  encuentra el mayor numero
#         if i > mayor:
#             mayor = i
#         # ejecuta el bucle y realiza la operacion
#     return cantidad, mayor

# def mostrar_resultados(cantidad, mayor):
#     print(f"Cantidad de numeros ingresados: {cantidad}")
#     print(f"Mayor numero ingresado: {mayor}")

# numeros = pedir_numeros(numeros)
# cantidad, mayor = analizar(numeros)
# mostrar_resultados(cantidad, mayor)

# # # prueba 2

# # numeros = []

# # def  pedir_numeros(numeros):
# #     print("Para finalizar el programa ingresa un numero negativo")
# #     numero = int(input("Ingresa un numero: "))
# #     while numero >= 0:
# #         numero = int(input("Ingresa un numero: "))
# #         numeros.append(numero)
# #     return numeros

# # def analizar(numeros):
# #     cantidad = len(numeros)
# #     mayor = max(numeros)
# #     return cantidad, mayor

# # numeros = pedir_numeros(numeros)
# # cantidad, mayor = analizar(numeros)

# # def mostrar_resultados(cantidad, mayor):
# #     print(f"La cantidad de numeros ingresados es: {cantidad}")
# #     print(f"El numero mayor del listado es: {mayor}")

# # mostrar_resultados(cantidad, mayor)

# # Escribí un programa que pida al usuario números enteros hasta que ingrese un número negativo. Al finalizar, mostrá cuántos números ingresó y cuál fue el mayor.

# # El programa debe organizarse con las siguientes funciones:
# # pedir_numeros()  → pide números al usuario y los devuelve en una lista.
# # analizar(numeros)  → recibe la lista y devuelve la cantidad y el mayor.
# # mostrar_resultados(cantidad, mayor)  → muestra los resultados por pantalla.

# numeros = []

# def pedir_numeros():
#     numero = int(input("ingresar numero"))
#     while numero >= 0:
#         numeros.append(numero)
#         numero = int(input("ingresar numero"))
#     return numeros

# numeros = pedir_numeros()

# def analizar(numeros):
#     cantidad = len(numeros)
#     mayor = max(numeros)
#     return cantidad, mayor

# cantidad, mayor = analizar(numeros)

# def mostrar_resultados(numeros, cantidad, mayor):
#     try:
#         with open("informe.txt", "w", encoding="utf-8") as archivo:
#             archivo.write(f"los numeros son {numeros}\n")
#             archivo.write(f"la cantidad de numeros es {cantidad}\n")
#             archivo.write(f"el mayor de los numeros es {mayor}\n")
#             print("el archivo se creo correctamente")
#     except OSError as error:
#         print(f"error al guardar el informe:{error}")

# mostrar_resultados(numeros, cantidad, mayor)