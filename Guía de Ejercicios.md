


## 🟢 Variables + IF (modelar situaciones)

---

### Ejercicio 1 — Clasificación de temperatura

Una estación meteorológica registra una temperatura ingresada por el usuario.

El programa debe:

- pedir una temperatura (número entero)
- indicar si es:
    - bajo cero (menor a 0)
    - templada (entre 0 y 25)
    - alta (mayor a 25)

👉 Extensión: validar que el dato ingresado sea numérico.

---

### Ejercicio 2 — Control de acceso por edad

Un sistema de acceso a un evento debe validar si una persona puede ingresar.

El programa debe:

- pedir la edad del usuario
- mostrar:
    - “Acceso denegado” si es menor a 18
    - “Acceso permitido” si tiene entre 18 y 64
    - “Acceso prioritario” si tiene 65 o más

👉 Analizar el caso borde: edad negativa.

---

### Ejercicio 3 — Comparación de productos

Un sistema de ventas recibe el precio de dos productos.

El programa debe:

- indicar cuál es más caro
- indicar si ambos tienen el mismo precio

👉 Extensión: mostrar la diferencia de precio.

---

## 🟡 FOR / WHILE (control del flujo)

---

### Ejercicio 4 — Generador de reporte

Un sistema debe mostrar un reporte de números del 1 al 20.

El programa debe:

- mostrar todos los números
- resaltar (imprimir aparte) los números pares

---

### Ejercicio 5 — Registro de ventas

Un comercio desea registrar ventas hasta que el usuario indique fin.

El programa debe:

- pedir montos de ventas
- finalizar cuando se ingrese 0
- mostrar:
    - cantidad de ventas
    - total vendido

---

### Ejercicio 6 — Validación de contraseña

Un sistema requiere autenticación.

El programa debe:

- pedir una contraseña
- repetir el pedido hasta que sea correcta ("admin123")
- mostrar “Acceso concedido”

👉 Extensión: contar cantidad de intentos.

---

## 🔵 Listas (manejo de múltiples datos)

---

### Ejercicio 7 — Registro de notas

Un docente carga las notas de 5 alumnos.

El programa debe:

- almacenar las notas en una lista
- mostrar todas las notas
- indicar cuántas son mayores o iguales a 6

---

### Ejercicio 8 — Análisis de datos

Dada una lista de números:

- calcular la suma total
- calcular el promedio
- indicar el valor máximo

---

### Ejercicio 9 — Búsqueda en inventario

Un sistema tiene una lista de productos (números o nombres).

El programa debe:

- pedir un producto
- indicar si existe o no en la lista

👉 Extensión: indicar en qué posición se encuentra.

---

### Ejercicio 10 — Limpieza de datos

Dada una lista de números con valores negativos:

- eliminar los números negativos
- mostrar la lista resultante

👉 ⚠️ Este ejercicio es clave para detectar errores de lógica.

---

## 🟣 Listas + WHILE (dinámico)

---

### Ejercicio 11 — Carga dinámica de datos

Un sistema debe registrar números ingresados por el usuario.

El programa debe:

- pedir números hasta ingresar 0
- almacenarlos en una lista

Luego:

- mostrar la lista completa
- mostrar solo los números positivos

---

### Ejercicio 12 — Estadísticas básicas

Usando la lista del ejercicio anterior:

- calcular:
    - suma
    - promedio
    - valor máximo
    - valor mínimo

---

## 🔴 Matrices

---

### Ejercicio 13 — Representación de datos

Un sistema representa datos en una matriz 3x3.

El programa debe:

- mostrar todos los valores
- imprimirlos en formato de tabla

---

### Ejercicio 14 — Filtrado de datos

Dada una matriz de números:

- mostrar solo los valores mayores a 10

---

### Ejercicio 15 — Procesamiento de matriz

El programa debe:

- calcular la suma de todos los elementos
- calcular el promedio total

---

### Ejercicio 16 — Análisis estructural

Dada una matriz 3x3:

- mostrar la diagonal principal
- calcular la suma de esa diagonal

---

## ⚫ Archivos

---

### Ejercicio 17 — Escritura de datos

Un sistema debe guardar información en un archivo.

El programa debe:

- pedir 5 números al usuario
- guardarlos en un archivo (uno por línea)

---

### Ejercicio 18 — Lectura de datos

El programa debe:

- leer el archivo anterior
- mostrar todos los valores almacenados

---

### Ejercicio 19 — Integración archivo + lista

El programa debe:

- leer un archivo con números
- guardarlos en una lista
- calcular:
    - suma
    - promedio

---

## 🧠 Integradores

---

### Ejercicio 20 — Sistema de análisis de datos

Desarrollar un programa que:

1. permita ingresar números hasta 0
2. los almacene en una lista
3. luego calcule:

- cantidad de datos
- suma total
- promedio
- cantidad de números pares

---

### Ejercicio 21 — Persistencia de datos

Extender el ejercicio anterior para:

- guardar los datos en un archivo
- luego leerlos desde el archivo
- mostrar nuevamente los resultados

---

### Ejercicio 22 — Sistema completo

Simular un sistema que:

1. permita ingresar datos numéricos
2. los almacene en una estructura
3. los procese
4. los persista en archivo

El programa debe mostrar:

- valores mayores a un umbral (ej: >10)
- promedio
- valor máximo
- cantidad de datos