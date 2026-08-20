def procesar_coleccion(lista_datos, funcion_transformacion, funcion_filtro):
    nueva_lista = []

    for dato in lista_datos:
        # Primero verificamos si cumple el filtro
        if funcion_filtro(dato):
            # Si cumple, aplicamos la transformación
            nuevo_dato = funcion_transformacion(dato)
            nueva_lista.append(nuevo_dato)

    return nueva_lista


# Lista con números pares y duplicados
datos = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8]

# Función de transformación: elevar al cuadrado
transformacion = lambda x: x ** 2

# Función de filtro: seleccionar solamente números pares
filtro = lambda x: x % 2 == 0


# Procesar la lista
resultado = procesar_coleccion(
    datos,
    transformacion,
    filtro
)

print("Lista original:", datos)
print("Lista resultante:", resultado)