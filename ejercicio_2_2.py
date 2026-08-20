# Código con BUG
def agregar_bitacora(mensaje, historial=[]):
    historial.append(mensaje)
    return historial


# Primera llamada
resultado1 = agregar_bitacora("Usuario inició sesión")
print("Primera llamada:", resultado1)

# Segunda llamada
resultado2 = agregar_bitacora("Usuario cerró sesión")
print("Segunda llamada:", resultado2)




#CORREGIDO
def agregar_bitacora(mensaje, historial=None):
    if historial is None:
        historial = []

    historial.append(mensaje)
    return historial


# Primera llamada
resultado1 = agregar_bitacora("Usuario inició sesión")
print("Primera llamada:", resultado1)

# Segunda llamada
resultado2 = agregar_bitacora("Usuario cerró sesión")
print("Segunda llamada:", resultado2)