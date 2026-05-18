matriz = []

def pedir_numeros():
    for i in range(3):
        fila = []
        for j in range(3):
            numeros = int(input("Ingresar numeros: "))
            fila.append(numeros)
        matriz.append(fila)
    return matriz
matriz = pedir_numeros()

def promediar(matriz):
    suma = 0
    cantidad = len(matriz)*len(matriz[0])
    for i in matriz:
        for j in i:
            suma += j
    promedio = suma/cantidad
    return promedio

promedio = promediar(matriz)

print("El promedio es: ", promedio)
print("La matriz es: ", matriz)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print(matriz[0][0])
print(matriz[1][2])
print(matriz[2][0])
print(f"La diagonal principal es: {matriz[0][0]}, {matriz[1][1]}, {matriz[2][2]}")

def crear_archivo(matriz):
    with open("matriz.txt", "w") as archivo:
        archivo.write(f"La matriz es: {matriz}\n")
        archivo.write(f"El promedio es: {promedio}\n")
        archivo.write(f"La diagonal principal es: {matriz[0][0]}, {matriz[1][1]}, {matriz[2][2]}\n")
        archivo.write(f"La matriz representada en filas es:\n")
        for fila in matriz:
            for numero in fila:
                archivo.write(f"{numero} ")
            archivo.write("\n")
crear_archivo(matriz)