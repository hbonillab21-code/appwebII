import math


class Estudiante:

    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []

    def agregar_calificacion(self, nota):
        if 0 <= nota <= 100:
            self.calificaciones.append(nota)
            print("Calificación agregada correctamente.")
        else:
            print("Error: la nota debe estar entre 0 y 100.")

    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0

        promedio = sum(self.calificaciones) / len(self.calificaciones)
        return math.ceil(promedio)

    def estado_final(self):
        promedio = self.calcular_promedio()

        if promedio >= 60:
            return "Aprobado"
        else:
            return "Reprobado"


nombre = input("Ingrese el nombre del estudiante: ")

estudiante = Estudiante(nombre)

cantidad = int(input("¿Cuántas calificaciones desea ingresar?: "))

for i in range(cantidad):
    nota = float(input(f"Ingrese la calificación {i + 1}: "))
    estudiante.agregar_calificacion(nota)

print("\n========== RESULTADO ==========")
print("Estudiante:", estudiante.nombre)
print("Calificaciones:", estudiante.calificaciones)
print("Promedio:", estudiante.calcular_promedio())
print("Estado final:", estudiante.estado_final())
print("===============================")

  