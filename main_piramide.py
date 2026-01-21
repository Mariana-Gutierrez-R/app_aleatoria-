import json
from consultas import contar_humanoides, nombre_y_raza, nombres_personajes
from piramide import imprimir_piramide_bloques

# Abrimos el JSON
with open("seed_races_personaje.json", encoding="utf-8") as f:
    personajes = json.load(f)

# Consulta 1: Cantidad de humanoides
humanoides = [str(contar_humanoides(personajes))]
print("Consulta 1: Cantidad de humanoides")
imprimir_piramide_bloques(humanoides, ancho_bloque=14)

# Consulta 2: Nombre y raza
nombres_raza = [f"{p['name']}:{p['race']}" for p in personajes]
print("\nConsulta 2: Nombre y raza")
imprimir_piramide_bloques(nombres_raza, max_personajes=50, ancho_bloque=14)

# Consulta 3: Nombres de personajes
nombres = [p['name'] for p in personajes]
print("\nConsulta 3: Nombres de personajes")
imprimir_piramide_bloques(nombres, max_personajes=50, ancho_bloque=14)