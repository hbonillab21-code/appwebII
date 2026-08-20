def aplicar_impuesto(tasa_iva, lista_precios):
    print("\n--- Dentro de la función, antes ---")
    print("Tasa IVA:", tasa_iva)
    print("Lista de precios:", lista_precios)

    # Intentamos modificar la tasa de IVA
    tasa_iva = tasa_iva + 0.05

    # Modificamos directamente la lista original
    for i in range(len(lista_precios)):
        lista_precios[i] = lista_precios[i] * (1 + tasa_iva)

    print("\n--- Dentro de la función, después ---")
    print("Tasa IVA:", tasa_iva)
    print("Lista de precios:", lista_precios)


# Datos iniciales
tasa_iva = 0.19
lista_precios = [10000, 20000, 30000]

print("--- Antes de llamar a la función ---")
print("Tasa IVA:", tasa_iva)
print("Lista de precios:", lista_precios)

# Llamar a la función
aplicar_impuesto(tasa_iva, lista_precios)

print("\n--- Después de llamar a la función ---")
print("Tasa IVA:", tasa_iva)
print("Lista de precios:", lista_precios)