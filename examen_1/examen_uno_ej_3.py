
# pide 5 notas al usuario y las devuelve en una lista
def pedir_notas():
    notas = []
    
    for i in range(5):
        i = int(input("Ingresa una nota: "))
        notas.append(i)
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

    estado = "aprueba" if promedio >= 6 else "no aprueba"

    try:
        with open("resultado.txt", "w", encoding="utf-8") as archivo:
            archivo.write(f"Promedio general: {promedio}\n")
            archivo.write(f"Estado del alumno: {estado}\n")
        print("El informe se guardó correctamente en resultado.txt")
    except OSError as error:
        print(f"No se pudo crear resultado.txt: {error}")


mostrar_informe(notas, aprobados, desaprobados, promedio, aprobados_count, desaprobados_count)



