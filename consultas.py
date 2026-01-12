# Ejemplos basicos de consultas con el json personajes.
# -------------------------------------------------------------------------------------------------
# Consulta 1: Mostrar todos los nombres de los personajes
import json

with open("seed_races_personaje.json", "r", encoding="utf-8") as f:
    personajes = json.load(f)

print("Nombres de todos los personajes")
for p in personajes:
    print(p.get("name"))


"""""
# Consulta 2: Mostrar el nombre y la raza
print("Nombre y raza de cada personaje")
for p in personajes:
    print(f"Name: {p.get('name')}, Race: {p.get('race')}")    

"""

""""
# Consulta 3: Personajes de "The Witcher"
print("Nombres de los personajes de The Witcher")
for p in personajes:
    if p.get("origin") == "The Witcher":
        print(f"Name: {p.get('name')}, Race: {p.get('race')}, Origin: {p.get('origin')}")
"""