# Ejemplos básicos de consultas con el json_personajes.
# -------------------------------------------------------------------------------------------------
def contar_humanoides(personajes):
    return sum(1 for p in personajes if p.get("category") == "Humanoide")


def nombre_y_raza(personajes):
    return [(p.get("name"), p.get("race")) for p in personajes]


def nombres_personajes(personajes):
    return [p.get("name") for p in personajes]