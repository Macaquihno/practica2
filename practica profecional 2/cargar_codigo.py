
def codigos(codigos):

    """
        Función que carga los códigos de trazabilidad.

        Pregunta al usuario la cantidad de códigos que desea ingresar.
        Pregunta al usuario que código desea ingresar en x posición.
        Agrega el código ingresado a la lista de códigos.

        Si el código ingresado es inválido, se le vuelve a preguntar al usuario que código desea ingresar en x posición.
        El sistema no pasará a la siguiente iteración si el código ingresado es inválido.
        """
    print("\n------- CARGAR CÓDIGOS -------")
    cantidad_codigos = int(input("Ingrese la cantidad de códigos que desea ingresar: "))

    for i in range(cantidad_codigos):
        valido = False
        while not valido:
            cadena_ingreso = str(input(f"Ingrese el código {i+1}: "))
            longitud = len(cadena_ingreso)

            if cadena_ingreso == "" or longitud < 4 and longitud:
                print("El código ingresado es inválido.")
            else:
                print("El código ingresado es válido.")
                codigos.append(cadena_ingreso)
                valido = True

    