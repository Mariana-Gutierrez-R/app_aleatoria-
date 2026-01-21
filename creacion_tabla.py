# Ejemplos básicos de consultas con el json_personajes.
# -------------------------------------------------------------------------------------------------

import json
import sqlite3

with open("seed_races_personaje.json", "r", encoding="utf-8") as f:
    personajes = json.load(f)

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("""
CREATE TABLE personajes (
    name text,
    race text,
    subrace text,
    category text,
    origin text,
    role text,
    weapon text,
    damage_type text,
    character text,
    morality text,
    threat_level text
)
""")

cur.executemany(
    "INSERT INTO personajes (name,race,subrace,category,origin,role,weapon,damage_type,character,morality,threat_level) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    [(x["name"], x["race"], x["subrace"],x["category"], x["origin"], x["role"], x["weapon"], x["damage_type"], x["character"], x["morality"], x["threat_level"]) for x in personajes]
)

rows = cur.execute("SELECT character, origin FROM personajes WHERE category = 'Humanoide'").fetchall()
print("Personajes humanoides")
print(rows)







"""
# Consulta 1: Contar cuántos humanoides hay

contador_humanoides = 0

for p in personajes:
    if p.get("category") == "Humanoide":
        contador_humanoides += 1

print("Cantidad de personajes humanoides:", contador_humanoides)


# Consulta 2: Mostrar el nombre y la raza

print("Nombre y raza de cada personaje")

for p in personajes:
    print(f"Name: {p.get('name')}, Race: {p.get('race')}")    

# Consulta 3: Mostrar todos los nombres de los personajes
print("Nombres de todos los personajes")
for p in personajes:
    print(p.get("name"))

"""