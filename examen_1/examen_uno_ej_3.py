
# pide 5 notas al usuario y las devuelve en una lista
def pedir_notas():
    notas = []
    for i in range(5):
        nota =  int(input("Ingresa una nota:"))
        notas.append(nota)
    return notas

# recibe la lista y devuelve el promedio

def filtrar_notas(notas):
    aprobados = []
    desaprobados = []
    for nota in notas:
        if nota >= 6:
            aprobados.append(nota)
        else:
            desaprobados.append(nota)
    return aprobados, desaprobados

def contar_notas(notas):
    aprobados = 0
    desaprobados = 0
    for nota in notas:
        if nota >= 6:
            aprobados += 1
        else:
            desaprobados += 1
    return aprobados, desaprobados

def sumar(notas):
    suma = 0
    for nota in notas:
        suma = suma + nota
    return suma


def calcular_promedio(notas):
    cantidad = len(notas)
    promedio = sumar(notas)/cantidad
    return promedio

notas = pedir_notas()
aprobados, desaprobados = filtrar_notas(notas)
promedio = calcular_promedio(notas)
aprobados_count, desaprobados_count = contar_notas(notas)
    
def mostrar_informe(notas, aprobados, desaprobados, promedio, aprobados_count, desaprobados_count):
    print(f"las notas ingresadas son {notas}")
    print(f"los aprobados son {aprobados}")
    print(f"los desaprobados son {desaprobados}")
    print(f"el promedio es general es {promedio}")
    print(f"Cantidad de aprobados: {aprobados_count}")
    print(f"Cantidad de desaprobados: {desaprobados_count}")

mostrar_informe(notas, aprobados, desaprobados, promedio, aprobados_count, desaprobados_count)
archivo = open("resultado.txt", "w")
archivo.write(f"las notas ingresadas son {notas}\n")
archivo.write(f"los aprobados son {aprobados}\n")
archivo.write(f"los desaprobados son {desaprobados}\n")
archivo.write(f"el promedio es general es {promedio}\n")
archivo.write(f"Cantidad de aprobados: {aprobados_count}\n")
archivo.write(f"Cantidad de desaprobados: {desaprobados_count}\n")
archivo.close()



