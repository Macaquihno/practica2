
def codigos(codigos):

    """
        Función que carga los códigos de trazabilidad.
        Pregunta al usuario la cantidad de códigos que desea ingresar,
        en que posicion y lo agrega a la lista de codigos.

        Si el código ingresado es inválido, se le vuelve a preguntar al usuario que código desea ingresar en x posición.
        El sistema no pasará a la siguiente iteración si el código ingresado es inválido.
        """
    print("\n------- CARGAR CÓDIGOS -------")
    cantidad_codigos = int(input("Ingrese la cantidad de códigos que desea ingresar: "))
    # Se solicita al usuario cuantos codigos quiere ingresar y lo vuelve un dato entero

    for i in range(cantidad_codigos):        # Repite el proceso tantas veces como codigos indico el usuario
        valido = False                       # Indica si el codigo es valido
        while not valido:              
            cadena_ingreso = str(input(f"Ingrese el código {i+1}: ")) # Solicita un codigo al ususario y lo vuelve dato string
            longitud = len(cadena_ingreso)   # Obtiene la cantidad de caracteres del codigo

            if cadena_ingreso == "" or longitud < 4 and longitud: # si el codigo esta vacio o tiene menos de 4 caracteres es invalido
                print("El código ingresado es inválido.")
            else:
                print("El código ingresado es válido.") # Si cumple los requisitos es validado
                codigos.append(cadena_ingreso)          # El codigo se agrega a la lista
                valido = True                           # Termina el While permitiendo pasar al siguiente codigo
 