def buscar_codigo(codigos):
    """
    Busca un código dentro de la lista
    y cuenta cuántas veces aparece.
    """

    codigo_buscar = input("Ingrese el código que desea buscar: ")

    encontrado = False
    cantidad = 0

    for codigo in codigos:
        if codigo == codigo_buscar:
            encontrado = True
            cantidad += 1

    if encontrado:
        print(f"El código '{codigo_buscar}' existe.")
        print(f"Aparece {cantidad} vez/veces.")
    else:
        print(f"El código '{codigo_buscar}' no existe.")