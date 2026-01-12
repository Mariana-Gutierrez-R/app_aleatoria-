import json

with open("seed_races.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print("JSON cargado correctamente")
print(datos)

