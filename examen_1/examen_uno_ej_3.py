
# # pide 5 notas al usuario y las devuelve en una lista
# def pedir_notas():
#     notas = []
    
#     for i in range(5):
#         i = int(input("Ingresa una nota: "))
#         notas.append(i)
#     return notas

# # recibe la lista y devuelve el promedio

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

# notas = pedir_notas()
# aprobados, desaprobados = filtrar_notas(notas)
# promedio = calcular_promedio(notas)
# aprobados_count, desaprobados_count = contar_notas(notas)
    
# def mostrar_informe(notas, aprobados, desaprobados, promedio, aprobados_count, desaprobados_count):
#     print(f"las notas ingresadas son {notas}")
#     print(f"los aprobados son {aprobados}")
#     print(f"los desaprobados son {desaprobados}")
#     print(f"el promedio es general es {promedio}")
#     print(f"Cantidad de aprobados: {aprobados_count}")
#     print(f"Cantidad de desaprobados: {desaprobados_count}")

#     estado = "aprueba" if promedio >= 6 else "no aprueba"

#     try:
#         with open("resultado.txt", "w", encoding="utf-8") as archivo:
#             archivo.write(f"Promedio general: {promedio}\n")
#             archivo.write(f"Estado del alumno: {estado}\n")
#         print("El informe se guardó correctamente en resultado.txt")
#     except OSError as error:
#         print(f"No se pudo crear resultado.txt: {error}")


# mostrar_informe(notas, aprobados, desaprobados, promedio, aprobados_count, desaprobados_count)


# Escribí un programa modular con las siguientes funciones:
# pedir_notas()  → pide 5 notas al usuario y las devuelve en una lista.
# calcular_promedio(notas)  → recibe la lista y devuelve el promedio.
# guardar_resultado(promedio)  → guarda en resultado.txt el promedio y si el alumno aprueba (>= 6) o no. Si el archivo no se puede crear, debe mostrar un mensaje de error en lugar de romperse.

# El programa principal debe llamar a las tres funciones en orden.


def pedir_notas():
    notas = []
    for i in range(5):
        i = int(input("pedir notas"))
        notas.append(i)
    cantidad = len(notas)
    return notas, cantidad

notas, cantidad = pedir_notas()

def calcular_promedio(notas):
    suma = 0
    for nota in notas:
        suma += nota
    promedio = suma/cantidad
    return promedio

promedio = calcular_promedio(notas)

def guardar_resultado(promedio):
    estado = "aprueba" if promedio >= 6 else "no aprueba"

    try:
        with open("resultados.txt", "w", encoding = "utf-8") as archivo:
            archivo.write(f"El promedio del estudiante es: {promedio}\n")
            archivo.write(f"Resultado de la asignatura: {estado}\n") 
        print("Se guardo correctamente el archivo")
    except OSError as error:
        print(f"El archivo no pudo guardarse - {error}")

guardar_resultado(promedio)
