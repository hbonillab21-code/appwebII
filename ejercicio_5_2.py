def ejecutar_mision(nombre_tarea, al_exito=None, al_error=None):
    try:
        print(f"Ejecutando tarea: {nombre_tarea}")

        # Simulamos una operación exitosa
        resultado = f"Tarea '{nombre_tarea}' completada correctamente"

        if al_exito:
            al_exito(nombre_tarea, resultado)

    except Exception as error:
        if al_error:
            al_error(nombre_tarea, str(error))


# Función que se ejecuta cuando todo sale bien
def tarea_exitosa(nombre, resultado):
    print(f"ÉXITO: {nombre}")
    print(f"Resultado: {resultado}")


# Función que se ejecuta cuando ocurre un error
def tarea_con_error(nombre, mensaje):
    print(f"ERROR en {nombre}: {mensaje}")


# Ejecutar la misión
ejecutar_mision(
    "Procesar datos",
    al_exito=tarea_exitosa,
    al_error=tarea_con_error
)