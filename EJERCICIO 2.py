
ventas_dia = [ "Electrónica","Ropa","Electrónica", "Hogar","Ropa","Electrónica","Juguetes","Hogar"
]

categorias_unicas = list(set(ventas_dia))

print("Categorías únicas:")
print(categorias_unicas)

conteo = {}

for categoria in ventas_dia:
    if categoria in conteo:
        conteo[categoria] += 1
    else:
        conteo[categoria] = 1

print("Cantidad de ventas por categoría:")
for categoria, cantidad in conteo.items():
    print(categoria, ":", cantidad)

categoria_mas_vendida = max(conteo, key=conteo.get)

print("\nCategoría más vendida:")
print(categoria_mas_vendida)

print("Cantidad de ventas:", conteo[categoria_mas_vendida])