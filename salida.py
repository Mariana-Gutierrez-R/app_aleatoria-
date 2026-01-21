def imprimir_resultado(titulo, datos):
    print("\n" + titulo)
    print("-" * len(titulo))

    if isinstance(datos, list):
        for fila in datos:
            if isinstance(fila, (list, tuple)):
                print(" | ".join(map(str, fila)))
            else:
                print(fila)
    else:
        print(datos)