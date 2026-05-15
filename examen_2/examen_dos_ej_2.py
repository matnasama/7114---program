# ejercicio 2

temperaturas = [22, 35, 18, 40, 15, 31, 28, 12, 38, 20]

def filtrar_calurosos(temperaturas):
    calurosos = []
    contador_calurosos = []
    for temp in temperaturas:
        if temp > 30:
            calurosos.append(temp)
    contador_calurosos = len(calurosos)
    return calurosos, contador_calurosos

calurosos, contador_calurosos = filtrar_calurosos(temperaturas)

def calcular_promedio(temperaturas):
    cantidad = len(temperaturas)
    suma = 0
    for temp in temperaturas:
        suma = suma + temp
        return suma
    promedio = suma/cantidad
    return promedio

promedio = calcular_promedio(temperaturas)

def mostrar_informe(contador_calurosos, promedio):
    print(f"La cantidad de días calurosos son: {contador_calurosos}")
    print(f"El promedio de temperatura es: {promedio}")

mostrar_informe(contador_calurosos, promedio)