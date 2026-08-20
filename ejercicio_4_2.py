def generar_reporte(titulo, secciones, *firmas):
    print(f"===== {titulo} =====")

    print("\nSecciones:")
    for seccion in secciones:
        print(f"- {seccion}")

    if firmas:
        print("\nFirmas:")
        for firma in firmas:
            print(f"- {firma}")


# Tupla con las secciones básicas
secciones_basicas = (
    "Introducción",
    "Objetivos",
    "Conclusiones"
)

# Lista con secciones adicionales
secciones_adicionales = [
    "Resultados",
    "Recomendaciones"
]

# Una sola llamada, desempaquetando ambas estructuras
generar_reporte(
    "Informe del Proyecto",
    [*secciones_basicas, *secciones_adicionales],
    "Harrinson Bonilla",
    "Profesor"
)