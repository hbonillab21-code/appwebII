def calcular_metricas(*numeros, **opciones):
    operacion = opciones.get("operacion", "suma")

    if operacion == "promedio":
        resultado = sum(numeros) / len(numeros)
    else:
        resultado = sum(numeros)

    if "redondear" in opciones:
        decimales = opciones["redondear"]

        if decimales is True:
            resultado = round(resultado)
        else:
            resultado = round(resultado, decimales)

    return resultado


print(calcular_metricas(10, 20, 30, operacion="suma"))
print(calcular_metricas(10, 20, 30, operacion="promedio"))
print(calcular_metricas(10, 20, 30, operacion="promedio", redondear=2))