
def analizar_longitudes(codigos):   # define la funcion recibiendo los codigos ingresados
    """
    Calcula la longitud total y el promedio de caracteres
    de los códigos almacenados.

    Parámetros:
        codigos (list): Lista de códigos de trazabilidad.
    """

    total_caracteres = 0            # Variable que acumulará la cantidad total de caracteres.

    for codigo in codigos:          # Recorre cada código de la lista.
        total_caracteres = total_caracteres + len(codigo)  # Suma la cantidad de caracteres por cada código al total.

    if len(codigos) > 0:            # Mientras haya mas de un codigo puede calcular el promedio
        promedio = total_caracteres / len(codigos)          # Divide el total de caracteres por la cantidad de códigos.
    else:
        promedio = 0                # Sin codigos el promedio es 0

    print("\n------- ANÁLISIS DE LONGITUDES -------")
    print(f"Total de caracteres: {total_caracteres}")
    print(f"Promedio de caracteres por código: {promedio}")

    # Muestra el total y el promedio de caracteres de los codigos
    