def buscar_clave_profunda(estructura, clave_objetivo):
    # Recorrer todas las claves del diccionario
    for clave, valor in estructura.items():

        # Si encontramos la clave que buscamos
        if clave == clave_objetivo:
            return valor

        # Si el valor es otro diccionario, buscamos dentro
        if isinstance(valor, dict):
            resultado = buscar_clave_profunda(valor, clave_objetivo)

            if resultado is not None:
                return resultado

    # Si no encontramos la clave
    return None


# Diccionario profundamente anidado
datos = {
    "usuario": {
        "nombre": "Carlos",
        "informacion": {
            "edad": 20,
            "direccion": {
                "ciudad": "Cartagena",
                "pais": "Colombia"
            }
        }
    }
}


print("Ciudad:", buscar_clave_profunda(datos, "ciudad"))
print("Edad:", buscar_clave_profunda(datos, "edad"))
print("País:", buscar_clave_profunda(datos, "pais"))
print("Teléfono:", buscar_clave_profunda(datos, "telefono"))