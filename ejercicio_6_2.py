def aplanar_lista(lista_anidada):
    resultado = []

    for elemento in lista_anidada:

        # Si encontramos otra lista, la aplanamos recursivamente
        if isinstance(elemento, list):
            resultado.extend(aplanar_lista(elemento))

        # Si no es una lista, agregamos el elemento
        else:
            resultado.append(elemento)

    return resultado


# Lista con diferentes niveles de profundidad
datos = [1, [2, [3, 4], 5], 6, [7]]

resultado = aplanar_lista(datos)

print("Lista original:")
print(datos)

print("\nLista aplanada:")
print(resultado)