# # Ejercicio 2 — Listas   (35 pts pts)
# # Trabajá con el siguiente listado de notas:


# # notas = [7, 3, 9, 5, 6, 2, 8]
# # Escribí un programa con las siguientes funciones:
# # filtrar_aprobados(notas)  → devuelve una lista con las notas mayores o iguales a 6.
# # calcular_promedio(notas)  → devuelve el promedio de toda la lista.
# # mostrar_informe(aprobados, promedio)  → muestra cuántos aprobaron, cuántos desaprobaron y el promedio general.
# # ⚠ Nota: No se aceptan soluciones sin funciones.

# notas = [7, 8, 9, 5, 6, 2, 8]

# def filtrar_notas(notas):
#     aprobados = []
#     desaprobados = []
#     for nota in notas:
#         if nota >= 6:
#             aprobados.append(nota)
#         else:
#             desaprobados.append(nota)
#     return aprobados, desaprobados

# def contar_notas(notas):
#     aprobados = 0
#     desaprobados = 0
#     for nota in notas:
#         if nota >= 6:
#             aprobados += 1
#         else:
#             desaprobados += 1
#     return aprobados, desaprobados

# def sumar(notas):
#     suma = 0
#     for nota in notas:
#         suma = suma + nota
#     return suma

# def calcular_promedio(notas):
#     cantidad = len(notas)
#     promedio = sumar(notas)/cantidad
#     return promedio

# aprobados, desaprobados = filtrar_notas(notas)
# promedio = calcular_promedio(notas)
# aprobados_count, desaprobados_count = contar_notas(notas)

# # print(f"los aprobados son {aprobados}")
# # print(f"el promedio es {promedio}")
    
# def mostrar_informe(aprobados, desaprobados, promedio, aprobados_count, desaprobados_count):
#     print(f"los aprobados son {aprobados}")
#     print(f"los desaprobados son {desaprobados}")
#     print(f"el promedio es general es {promedio}")
#     print(f"Cantidad de aprobados: {aprobados_count}")
#     print(f"Cantidad de desaprobados: {desaprobados_count}")

# mostrar_informe(aprobados, desaprobados, promedio, aprobados_count, desaprobados_count)

# # prueba 2
# # examen 1 ejercicio 2
# # Trabajá con el siguiente listado de notas:


# # notas = [7, 3, 9, 5, 6, 2, 8]
# # Escribí un programa con las siguientes funciones:
# # filtrar_aprobados(notas)  → devuelve una lista con las notas mayores o iguales a 6.
# # calcular_promedio(notas)  → devuelve el promedio de toda la lista.
# # mostrar_informe(aprobados, promedio)  → muestra cuántos aprobaron, cuántos desaprobaron y el promedio general.
# # ⚠ Nota: No se aceptan soluciones sin funciones.

# notas = [7, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 1]

# def filtrar_aprobados(notas):
#     aprobados = []
#     desaprobados = []
#     for nota in notas:
#         if nota >= 6:
#             aprobados.append(nota)
#         else:
#             desaprobados.append(nota)
#     aprobados_total = len(aprobados)
#     desaprobados_total = len(desaprobados)
#     return aprobados, desaprobados, aprobados_total, desaprobados_total

# aprobados, desaprobados, aprobados_total, desaprobados_total = filtrar_aprobados(notas)

# def calcular_promedio(notas):
#     cantidad = len(notas)
#     suma = 0
#     for nota in notas:
#         suma += nota
#     promedio = suma/cantidad
#     return promedio

# promedio = calcular_promedio(notas)


# def mostrar_informe(aprobados, desaprobados, aprobados_total, desaprobados_total, promedio):
#     print(f"Los aprobados son :{aprobados}")
#     print(f"La cantidad de aprobados es:{aprobados_total}")
#     print(f"Los desaprobados son :{desaprobados}")
#     print(f"La cantidad de desaprobados es: {desaprobados_total}")
#     print(f"El promedio general es :{promedio}")
#     return(
#         f"Los aprobados son: {aprobados}\n"
#         f"La cantidad de aprobados es: {aprobados_total}\n"
#         f"Los desaprobados son: {desaprobados}\n"
#         f"La cantidad de desaprobados es: {desaprobados_total}\n"
#         f"El promedio general es: {promedio}\n"
#     )

# archivo = open("informe.txt", "w")
# archivo.write(
#     mostrar_informe(
#         aprobados,
#         desaprobados,
#         aprobados_total,
#         desaprobados_total,
#         promedio))
# archivo.close()

# Trabajá con el siguiente listado de notas:

# notas = [7, 3, 9, 5, 6, 2, 8]
# Escribí un programa con las siguientes funciones:
# filtrar_aprobados(notas)  → devuelve una lista con las notas mayores o iguales a 6.
# calcular_promedio(notas)  → devuelve el promedio de toda la lista.
# mostrar_informe(aprobados, promedio)  → muestra cuántos aprobaron, cuántos desaprobaron y el promedio general.
# ⚠ Nota: No se aceptan soluciones sin funciones.

# notas = [7, 3, 9, 5, 6, 2, 8]

# def filtrar_aprobados(notas):
#     aprobados = []
#     desaprobados = []
#     for i in notas:
#         if i >= 6:
#             aprobados.append(i)
#         else:
#             desaprobados.append(i)
#     count_aprobados = len(aprobados)
#     count_desaprobados = len(desaprobados)
#     return aprobados, desaprobados, count_aprobados, count_desaprobados

# aprobados, desaprobados, count_aprobados, count_desaprobados = filtrar_aprobados(notas)

# def calcular_promedio(notas):
#     cantidad = len(notas)
#     suma = 0
#     for i in notas:
#         suma += i
#         promedio = suma/cantidad
#     return promedio

# promedio = calcular_promedio(notas)

# def mostrar_informe(count_aprobados,count_desaprobados, promedio):
#     try:
#         with open("informe_final.txt", "w", encoding="utf-8") as archivo:
#             archivo.write(f"La cantidad de aprobados es: {count_aprobados}\n")
#             archivo.write(f"La cantidad de desaprobados es: {count_desaprobados}\n")
#             archivo.write(f"El promedio general es: {promedio}\n")
#         print("El archivo se genero correctamente")
#     except OSError as error:
#         print(f"Hubo en error en la creacion del archivo: {error}")

# mostrar_informe(count_aprobados, count_desaprobados, promedio)