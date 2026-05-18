# matriz = []

# def pedir_numeros():
#     for i in range(3):
#         fila = []
#         for j in range(3):
#             numeros = int(input("Ingresar numeros: "))
#             fila.append(numeros)
#         matriz.append(fila)
#     return matriz
# matriz = pedir_numeros()

# def promediar(matriz):
#     suma = 0
#     cantidad = len(matriz)*len(matriz[0])
#     for i in matriz:
#         for j in i:
#             suma += j
#     promedio = suma/cantidad
#     return promedio

# promedio = promediar(matriz)

# print("El promedio es: ", promedio)
# print("La matriz es: ", matriz)
# print(matriz[0])
# print(matriz[1])
# print(matriz[2])
# print(matriz[0][0])
# print(matriz[1][2])
# print(matriz[2][0])
# print(f"La diagonal principal es: {matriz[0][0]}, {matriz[1][1]}, {matriz[2][2]}")

# def crear_archivo(matriz):
#     with open("matriz.txt", "w") as archivo:
#         archivo.write(f"La matriz es: {matriz}\n")
#         archivo.write(f"El promedio es: {promedio}\n")
#         archivo.write(f"La diagonal principal es: {matriz[0][0]}, {matriz[1][1]}, {matriz[2][2]}\n")
#         archivo.write(f"La matriz representada en filas es:\n")
#         for fila in matriz:
#             for numero in fila:
#                 archivo.write(f"{numero} ")
#             archivo.write("\n")
# crear_archivo(matriz)

# def pedir_numeros():
#     numeros = []
#     for i in range(3):
#         fila = []
#         for j in range(3):
#             numero = int(input("Ingresar un numero: "))
#             fila.append(numero)
#         numeros.append(fila)
#     return numeros

# numeros = pedir_numeros()
# print(numeros)

# def calcular_promedio(numeros):
#     cantidad = len(numeros)*len(numeros[0])
#     suma = 0
#     for fila in numeros:
#         for numero in fila:
#             suma += numero
#     print(cantidad)
#     print(suma)
#     promedio = suma/cantidad
#     return promedio

# promedio = calcular_promedio(numeros)

# def mostrar_resultados(numeros, promedio):
#     print(f"La matriz de numeros es: {numeros}\n")
#     print(f"El promedio de los numeros es: {promedio}\n")  
#     print(f"{numeros[0]}\n")
#     print(f"{numeros[1]}\n")
#     print(f"{numeros[2]}\n")
#     for fila in numeros:
#         for numero in fila:
#             print(f"{numero}")
#         print(f"\n")
#     try:
#         with open("matmedio.txt", "w", encoding="utf-8") as archivo:
#             archivo.write(f"La matriz de numeros es: {numeros}\n")
#             archivo.write(f"El promedio de la matriz es: {promedio}\n")
#             archivo.write(f"{numeros[0]}\n")
#             archivo.write(f"{numeros[1]}\n")
#             archivo.write(f"{numeros[2]}\n")
#             for fila in numeros:
#                 for numero in fila:
#                     archivo.write(f"{numero}")
#                 archivo.write(f"\n")
#             print(f"El archivo se creo correctamente")
#     except OSError as error:
#         print(f"El archivo no se creo correctamente - {error}")

# mostrar_resultados(numeros, promedio)