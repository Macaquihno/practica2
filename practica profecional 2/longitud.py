
def analizar_longitudes(codigos):
    """
    Calcula la longitud total y el promedio de caracteres
    de los códigos almacenados.

    Parámetros:
        codigos (list): Lista de códigos de trazabilidad.

    Retorno:
        None
    """

    total_caracteres = 0

    for codigo in codigos:
        total_caracteres = total_caracteres + len(codigo)

    if len(codigos) > 0:
        promedio = total_caracteres / len(codigos)
    else:
        promedio = 0

    print("\n------- ANÁLISIS DE LONGITUDES -------")
    print(f"Total de caracteres: {total_caracteres}")
    print(f"Promedio de caracteres por código: {promedio}")