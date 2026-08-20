def conectar_api(url, timeout=30, retries=3, use_ssl=True):
    return f"Conexión a {url} | timeout={timeout}s | retries={retries} | use_ssl={use_ssl}"


# Usando los valores por defecto
resultado1 = conectar_api("https://api.ejemplo.com")

print(resultado1)


# Cambiando algunos valores
resultado2 = conectar_api(
    "https://api.ejemplo.com",
    timeout=60,
    retries=5,
    use_ssl=False
)

print(resultado2)