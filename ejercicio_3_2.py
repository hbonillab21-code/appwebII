def auditar_evento(nivel, *etiquetas, **metadatos):

    mensaje = f"[{nivel.upper()}]"

    if etiquetas:
        mensaje += " Tags: " + ", ".join(f"#{tag}" for tag in etiquetas)

    if metadatos:
        datos = ", ".join(f"{clave}: {valor}" for clave, valor in metadatos.items())
        mensaje += f" | Metadatos -> {datos}"

    print(mensaje)


# Ejemplo completo
auditar_evento(
    "error",
    "seguridad",
    "auth",
    usuario="admin",
    ip="192.168.1.50",
    intento=3
)

# Solo nivel
auditar_evento("info")

# Nivel y etiquetas
auditar_evento("warning", "servidor", "cpu")