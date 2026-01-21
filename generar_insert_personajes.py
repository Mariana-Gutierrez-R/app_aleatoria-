import json

with open("seed_races_personaje.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def esc(s):
    if s is None:
        return "NULL"
    s = str(s).replace("\\", "\\\\").replace("'", "''")
    return f"'{s}'"

sql = []
sql.append("USE seed_races;")
sql.append("")
sql.append(
    "INSERT INTO personajes "
    "(name, race, subrace, category, origin, role, weapon, damage_type, character_name, morality, threat_level)"
)
sql.append("VALUES")

values = []
for item in data:
    values.append("(" + ", ".join([
        esc(item.get("name")),
        esc(item.get("race")),
        esc(item.get("subrace")),
        esc(item.get("category")),
        esc(item.get("origin")),
        esc(item.get("role")),
        esc(item.get("weapon")),
        esc(item.get("damage_type")),
        esc(item.get("character")),   # JSON → character
        esc(item.get("morality")),
        esc(item.get("threat_level")),
    ]) + ")")

sql.append(",\n".join(values) + ";")

with open("insert_personajes.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(sql))

print("✅ Archivo insert_personajes.sql creado con", len(data), "personajes.")