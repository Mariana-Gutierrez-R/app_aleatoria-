# piramide.py

def imprimir_piramide_bloques(lista_datos, max_personajes=150, ancho_bloque=12):
    """
    Imprime los elementos de lista_datos en forma de pirámide
    cada elemento dentro de un bloque tipo ladrillo.
    ancho_bloque: ancho de cada bloque en caracteres
    """
    # Limitamos la cantidad de datos
    lista_datos = lista_datos[:max_personajes]

    n = len(lista_datos)
    fila = 1
    indice = 0

    while indice < n:
        # Número de bloques en esta fila
        bloques_fila = min(fila, n - indice)
        fila_nombres = lista_datos[indice: indice + bloques_fila]

        # Construimos cada bloque
        bloques = []
        for name in fila_nombres:
            nombre_centrado = f"{name[:ancho_bloque-4]:^{ancho_bloque-4}}"  # recortar y centrar
            bloque = f"|{nombre_centrado}|"
            bloques.append(bloque)

        # Construimos la fila con separación entre bloques
        fila_str = " ".join(bloques)
        # Centrar la fila
        print(fila_str.center(80))
        # Separador inferior de los bloques
        fila_sep = " ".join(["-"*ancho_bloque for _ in fila_nombres])
        print(fila_sep.center(80))

        indice += bloques_fila
        fila += 1