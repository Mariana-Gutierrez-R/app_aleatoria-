import json

from consultas import contar_humanoides, nombre_y_raza, nombres_personajes
from salida import imprimir_resultado

with open("seed_races_personaje.json", encoding="utf-8") as f:
    personajes = json.load(f)

imprimir_resultado(
    "Consulta 1: Cantidad de humanoides",
    contar_humanoides(personajes)
)

imprimir_resultado(
    "Consulta 2: Nombre y raza",
    nombre_y_raza(personajes)
)

imprimir_resultado(
    "Consulta 3: Nombres de personajes",
    nombres_personajes(personajes)
)