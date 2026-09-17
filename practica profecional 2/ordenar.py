def mostrar_codigos_ordenados(codigos):
    """
    Ordena y muestra los códigos utilizando el método de Burbuja.
    Parámetros:
        codigos (list): Lista de códigos de trazabilidad.
    Retorno:
        None
    """
    lista_ordenada = codigos[:]

    # Método de Burbuja
    for i in range(len(lista_ordenada) - 1):
        for j in range(len(lista_ordenada) - 1 - i):

            if lista_ordenada[j] > lista_ordenada[j + 1]:
                auxiliar = lista_ordenada[j]
                lista_ordenada[j] = lista_ordenada[j + 1]
                lista_ordenada[j + 1] = auxiliar

    print("\n------- CÓDIGOS ORDENADOS -------")

    for codigo in lista_ordenada:
        print(codigo)
        