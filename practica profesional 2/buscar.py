def buscar_codigo(codigos):
    """
    Busca un código dentro de la lista
    y cuenta cuántas veces aparece.
    """
    print("\n------- BUSCAR CÓDIGOS -------")
    
    codigo_buscar = input("Ingrese el código que desea buscar: ") 
    #Ingresa input sobre el codigo que desea buscar; verifica si existe este mismo

    encontrado = False   # Variable indica si se encuentra el codigo
    cantidad = 0         # Variable cuenta cuantas veces aparece

    for codigo in codigos:            # Recorre todos los codigos
        if codigo == codigo_buscar:   # Si el codigo que buscas es igual a un codigo existente
            encontrado = True         # Es encontrado
            cantidad += 1             # Se suma a la cantidad de veces que aparece

    if encontrado:       # Si aparece se indica que existe y cuantas veces aparece
        print(f"El código '{codigo_buscar}' existe.")
        print(f"Aparece {cantidad} vez/veces.")
    else:                # Si no aparece se da a entender que no existe
        print(f"El código '{codigo_buscar}' no existe.")