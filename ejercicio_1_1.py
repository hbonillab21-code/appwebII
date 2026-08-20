def crear_perfil_usuario(nombre, email, rol):
    if "@" not in email:
        return "Error: el email debe contener el símbolo @."

    perfil = {
        "nombre": nombre,
        "email": email,
        "rol": rol
    }

    return perfil


# Primer caso
resultado1 = crear_perfil_usuario(
    "Laura Gomez",
    "laura@empresa.com",
    "Desarrolladora"
)

print(resultado1)


# Segundo caso
resultado2 = crear_perfil_usuario(
    rol="Admin",
    nombre="Carlos",
    email="carlos_sin_arroba"
)

print(resultado2)