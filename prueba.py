
# def pedir_numeros():
#     numeros = []
#     numero = int(input("Ingresar un numero: "))
#     while numero >= 0:
#         numeros.append(numero)
#         numero = int(input("Ingresar un numero: "))
#     return numeros

# numeros =  pedir_numeros()

# def analizar_numeros(numeros):
#     cantidad = len(numeros)
#     mayor = max(numeros)
#     return cantidad, mayor

# cantidad, mayor = analizar_numeros(numeros)

# def mostrar_resultados(cantidad, mayor, numeros):
#     print(f"La cantidad de numeros es: {cantidad}")
#     print(f"El mayor de los numeros es: {mayor}")
#     print(f"El listado de numeros recibidos es: {numeros}")
    
# mostrar_resultados(cantidad, mayor, numeros)

# notas = [7, 3, 9, 5, 6, 2, 8, 4, 10, 1]

# def filtrar_aprobados(notas):
#     aprobados = []
#     desaprobados = []
#     for nota in notas:
#         if nota >= 6:
#             aprobados.append(nota)
#         else:
#             desaprobados.append(nota)
#     aprobados = len(aprobados)
#     desaprobados = len(desaprobados)            
#     return aprobados, desaprobados

# aprobados, desaprobados = filtrar_aprobados(notas)

# def calcular_promedio(notas):
#     cantidad = len(notas)
#     suma = 0
#     for nota in notas:
#         suma += nota
#     promedio = suma/cantidad
#     return promedio

# promedio = calcular_promedio(notas)

# def mostrar_resultados(aprobados, desaprobados, promedio):
#     print(f"La cantidad de aprobados es: {aprobados}")
#     print(f"La cantidad de desaprobados es: {desaprobados}")
#     print(f"El promedio de las notas es:{promedio}")
    
# mostrar_resultados(aprobados, desaprobados, promedio)

# def pedir_notas():
#     notas = []
#     for nota in range(5):
#         nota = int(input("Ingresar nota: "))
#         notas.append(nota)
#     return notas

# notas = pedir_notas()

# def calcular_promedio(notas):
#     cantidad = len(notas)
#     suma = 0
#     for nota in notas:
#         suma += nota
#     promedio =  suma/cantidad
#     return promedio

# promedio = calcular_promedio(notas)

# def guardar_resultado(promedio):
#     estado = "aprobado" if promedio >= 6 else "desaprobado"

#     try:
#         with open("resultado.txt", "w", encoding="utf-8") as archivo:
#             archivo.write(f"El promedio del estudiante es: {promedio}\n")
#             archivo.write(f"El resultado de la asignatura es: {estado}\n")
#         print(f"El archivo se creo correctamente")
#     except OSError as error:
#         print(f"El archivo no se creo correctamente - {error}")

# guardar_resultado(promedio)

# def pedir_palabras():
#     palabras = []
#     palabra = input("Ingresa unas palabras: ")
#     while palabra != "fin":
#         palabras.append(palabra)
#         palabra = input("Ingresa unas palabras: ")
#     return palabras

# palabras =  pedir_palabras()

# def analizar_palabras(palabras):
#     cantidad = len(palabras)
#     palabra_larga = max(palabras)
#     return cantidad, palabra_larga

# cantidad, palabra_larga = analizar_palabras(palabras)

# def mostrar_resultados(cantidad, palabra_larga):
#     print(f"la cantidad de palabras es: {cantidad}\n")
#     print(f"la palabra mas larga es: {palabra_larga}")

# mostrar_resultados(cantidad, palabra_larga)


# def pedir_productos():
#     productos = []
#     for producto in range(5):
#         producto = input("Ingresar un producto: ")
#         productos.append(producto)
#     return productos

# productos = pedir_productos()

# def analizar_productos(productos):
#     cantidad = len(productos)
#     primero = min(productos)
#     return cantidad, primero

# cantidad, primero = analizar_productos(productos)

# def guardar_reporte(productos, cantidad, primero):
#     try:
#         with open("inventario.txt", "w", encoding="utf-8") as archivo:
#             archivo.write(f"Los productos son los siguientes: {productos}\n")
#             archivo.write(f"La cantidad de productos en la lista es: {cantidad}\n")
#             archivo.write(f"El primero de los productos alfabeticamente es: {primero}\n")
#         print(f"El archivo se creo correctamente")    
#     except OSError as error:
#         print(f"El archivo no se creo correctamente - {error}")

# guardar_reporte(productos, cantidad, primero)