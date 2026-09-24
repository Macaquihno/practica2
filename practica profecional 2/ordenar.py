def mostrar_codigos_ordenados(codigos): # define funcion recibiendo los codigos ingresados
    """
    Ordena y muestra los códigos utilizando el método de Burbuja.
    Parámetros: codigos (list): Lista de códigos de trazabilidad.
    """
    lista_ordenada = codigos[:] # Se copia la lista original en una nueva variable

    # Método de Burbuja
    for i in range(len(lista_ordenada) - 1):  # por cada elemento en la lista se repite el procedimiento
        for j in range(len(lista_ordenada) - 1 - i): # compara cada elemento de la lista

            if lista_ordenada[j] > lista_ordenada[j + 1]: # si el primer elemento es mayor a su siguiente
                auxiliar = lista_ordenada[j]              # guarda temporalmente el primer elemento
                lista_ordenada[j] = lista_ordenada[j + 1] # coloca el menor en la posicion anterior
                lista_ordenada[j + 1] = auxiliar          # coloca el mayor en la posicion siguiente

    print("\n------- CÓDIGOS ORDENADOS -------")

    for codigo in lista_ordenada:
        print(codigo)
        #Recorre la lista mostrando cada codigo ordenado