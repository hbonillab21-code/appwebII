
nombre = input("Ingrese el nombre del cliente: ")
precio = float(input("Ingrese el precio base del producto: "))
cantidad = int(input("Ingrese la cantidad adquirida: "))


vip = input("¿Tiene membresía VIP? (si/no): ").lower() == "si"


total = precio * cantidad


if cantidad >= 5 and vip:
    descuento = 25
elif cantidad >= 5 or vip:
    descuento = 15
else:
    descuento = 0

valor_descuento = total * descuento / 100
total_pagar = total - valor_descuento


print("\n========== RESUMEN DEL COBRO ==========")
print("Cliente:", nombre)
print("Precio del producto: $", precio)
print("Cantidad adquirida:", cantidad)
print("Membresía VIP:", vip)
print("Total sin descuento: $", total)
print("Descuento aplicado:", descuento, "%")
print("Valor del descuento: $", valor_descuento)
print("TOTAL A PAGAR: $", total_pagar)
print("=======================================")