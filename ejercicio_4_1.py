def inicializar_db(host, puerto, db_name, usuario, password):
    print("Conectando a la base de datos...")
    print(f"Host: {host}")
    print(f"Puerto: {puerto}")
    print(f"Base de datos: {db_name}")
    print(f"Usuario: {usuario}")
    print("Conexión configurada correctamente.")


config = {
    "host": "cluster-db.internal",
    "puerto": 5432,
    "db_name": "production_v2",
    "usuario": "app_user",
    "password": "S3cur3P@ss!"
}


# Desempaquetar el diccionario con **
inicializar_db(**config)