# Escribí un programa modular con las siguientes funciones:

# pedir_productos()  → pide al usuario el nombre de 5 productos y los devuelve en una lista.
# analizar_productos(productos)  → recibe la lista y devuelve la cantidad de productos y el primero en orden alfabético.
# guardar_reporte(productos, cantidad, primero)  → guarda en inventario.txt la lista de productos, la cantidad y el primero alfabéticamente. Si el archivo no se puede crear, debe mostrar un mensaje de error en lugar de romperse.
# El programa principal debe llamar a las tres funciones en orden.

productos = []

def pedir_productos(productos):
    producto = 0
    for producto in range(5):
        producto = input("Ingresá el nombre del producto: ")
        productos.append(producto)
    return productos

def analizar_productos(productos):
    cantidad = len(productos)
    alfabetico = sorted(productos)[0]
    return cantidad, alfabetico

productos = pedir_productos(productos)
cantidad, alfabetico = analizar_productos(productos)

def guardar_reporte(productos, cantidad, alfabetico):
    archivo = open("inventario.txt", "w")
    archivo.write(f"La lista de productos es: {productos}\n")
    archivo.write(f"La cantidad de productos es: {cantidad}\n")
    archivo.write(f"El primer de producto es: {alfabetico}\n")
    archivo.close()

guardar_reporte(productos, cantidad, alfabetico)