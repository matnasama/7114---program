# # ejercicio 2

# temperaturas = [22, 35, 18, 40, 15, 31, 28, 12, 38, 20]

# def filtrar_calurosos(temperaturas):
#     calurosos = []
#     contador_calurosos = []
#     for temp in temperaturas:
#         if temp > 30:
#             calurosos.append(temp)
#     contador_calurosos = len(calurosos)
#     return calurosos, contador_calurosos

# calurosos, contador_calurosos = filtrar_calurosos(temperaturas)

# def calcular_promedio(temperaturas):
#     cantidad = len(temperaturas)
#     suma = 0
#     for temp in temperaturas:
#         suma = suma + temp
#         return suma
#     promedio = suma/cantidad
#     return promedio

# promedio = calcular_promedio(temperaturas)

# def mostrar_informe(contador_calurosos, promedio):
#     print(f"La cantidad de días calurosos son: {contador_calurosos}")
#     print(f"El promedio de temperatura es: {promedio}")

# mostrar_informe(contador_calurosos, promedio)

# Trabajá con el siguiente listado de temperaturas diarias (en °C):


# temperaturas = [22, 35, 18, 40, 15, 31, 28, 12, 38, 20]
# Escribí un programa con las siguientes funciones:
# filtrar_calurosos(temperaturas)  → devuelve una lista solo con las temperaturas mayores a 30°C.
# calcular_promedio(temperaturas)  → devuelve el promedio de todas las temperaturas.
# mostrar_informe(calurosos, promedio)  → muestra cuántos días calurosos hubo, cuántos no, y el promedio.
# ⚠ Nota: No se aceptan soluciones sin funciones.

temperaturas = [22, 35, 38, 40, 15, 31, 28, 32, 38, 20]

def filtrar_calurosos(temperaturas):
    dias_totales = len(temperaturas)
    calurosos = []
    no_calurosos = []
    for temp in temperaturas:
        if temp > 30:
            calurosos.append(temp)
        else:
            no_calurosos.append(temp)
    count_calurosos = dias_totales - len(no_calurosos)
    count_no_calurosos = dias_totales - len(calurosos)
    return dias_totales, calurosos, no_calurosos,count_calurosos, count_no_calurosos

dias_totales, calurosos, no_calurosos, count_calurosos, count_no_calurosos = filtrar_calurosos(temperaturas)

def calcular_promedio(temperaturas):
    suma = 0
    for temp in temperaturas:
        suma += temp
    promedio = suma/dias_totales
    return promedio

promedio = calcular_promedio(temperaturas)

def mostrar_informe(calurosos, no_calurosos, count_calurosos, count_no_calurosos, promedio):
    print(f"Los dias calurosos son: {calurosos}")
    print(f"Los dias no calurosos son: {no_calurosos}")
    print(f"Los dias calurosos son: {count_calurosos}")
    print(f"Los dias no calurosos son: {count_no_calurosos}")
    print(f"La temperatura promedio es: {promedio}")
    try:
        with open("temperaturas.txt", "w", encoding = "utf-8") as archivo:
            archivo.write(f"Los dias calurosos son: {count_calurosos}\n")
            archivo.write(f"Los dias no calurosos son: {count_no_calurosos}\n")    
            archivo.write(f"La temperatura promedio es: {promedio}\n")
        print(f"El archivo se creo correctamente")
    except OSError as error:
        print(f"El archivo no se creo correctamente - {error}")

mostrar_informe(calurosos, no_calurosos, count_calurosos, count_no_calurosos, promedio)